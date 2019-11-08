#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# Keybase has added an encrypted key-value store; see 4_simple_storage.py for
# more information.
#
# This example implements a simple bot to manage hackerspace tool rentals. It
# shows one way you can obfuscate entryKeys (which are not encrypted) by
# storing their HMACs, so that no one but your team (not even
# Keybase) can know about the names of all the cool tools you have; you can do
# something similar to hide namespaces. Additionally this example handles
# concurrent writes using a cache to prevent one user from unintentionally
# clobbering another user's rental updates.
# ###################################

import asyncio
import hmac
import json
import logging
import os
import secrets
import sys
from base64 import b64decode, b64encode
from enum import Enum
from typing import Any, Dict, List, Union

from pykeybasebot import Bot, EventType, KVStoreClient
from pykeybasebot.errors import DeleteNonExistentError, RevisionError
from pykeybasebot.types import keybase1

logging.basicConfig(level=logging.DEBUG)

if "win32" in sys.platform:
    # Windows specific event-loop policy
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy()  # type: ignore
    )


class CachedBot(Bot):
    """
        Custom bot maintains a cache of secrets for
        SecretKeyKVStoreClients.
    """

    @property
    def secret_kvstore(self):
        if not hasattr(self, "secret"):
            # secrets = {team: {namespace: secret}}
            self.secrets: Dict[str, Dict[str, bytes]] = {}
        return SecretKeyKVStoreClient(self)


class SecretKeyKVStoreClient(KVStoreClient):
    """
        A KVStoreClient that hides the entryKeys from Keybase servers.

        It does so by HMACing entryKeys using a per-(team, namespace) secret,
        and storing the HMAC instead of the plaintext entryKey. This approach
        does not handle any secret rotation, and does not expect the secret to
        change.

        The plaintext entryKey is stored in it's corresponding JSON entryValue
        under the key "_key" to enable listing.

        This approach does not hide memory access patterns. Also, Keybase
        servers prevent a removed team member from continuing to access a team's
        data, but if that were somehow bypassed*, a former team member who still
        knows the HMAC secret can check for the presence of specific entryKeys
        (*but you probably have bigger issues to deal with in that case...).
    """

    KEY_KEY = "_key"
    SECRET_KEY = "_secret"
    SECRET_NUM_BYTES = 32

    def __init__(self, bot):
        self.secrets = bot.secrets
        super().__init__(bot)

    async def load_secret(self, team, namespace) -> bytes:
        if team not in self.secrets or namespace not in self.secrets[team]:
            secret = secrets.token_bytes(self.SECRET_NUM_BYTES)
            try:
                # we don't expect self.SECRET_KEY's revision > 0
                await super().put(
                    team, namespace, self.SECRET_KEY, bytes_to_str(secret), revision=1
                )
            except RevisionError:
                res: keybase1.KVGetResult = await super().get(
                    team, namespace, self.SECRET_KEY
                )
                secret = str_to_bytes(res.entry_value)
            # update self.secrets (which also updates self.bot.secrets)
            if team not in self.secrets:
                self.secrets[team] = {}
            self.secrets[team][namespace] = secret
        return self.secrets[team][namespace]

    async def hmac_key(self, team, namespace, entryKey) -> str:
        secret = await self.load_secret(team, namespace)
        return hmac.new(secret, entryKey.encode("utf-8")).hexdigest()

    async def put(
        self,
        team: str,
        namespace: str,
        entryKey: str,
        entryValue: str,
        revision: Union[int, None] = None,
    ) -> keybase1.KVPutResult:
        h = await self.hmac_key(team, namespace, entryKey)
        res = await super().put(team, namespace, h, entryValue, revision)
        res.entry_key = entryKey
        return res

    async def delete(
        self,
        team: str,
        namespace: str,
        entryKey: str,
        revision: Union[int, None] = None,
    ) -> keybase1.KVDeleteEntryResult:
        h = await self.hmac_key(team, namespace, entryKey)
        res = await super().delete(team, namespace, h, revision)
        res.entry_key = h
        return res

    async def get(
        self, team: str, namespace: str, entryKey: str
    ) -> keybase1.KVGetResult:
        h = await self.hmac_key(team, namespace, entryKey)
        res = await super().get(team, namespace, h)
        res.entry_key = h
        return res

    async def list_entrykeys(
        self, team: str, namespace: str
    ) -> keybase1.KVListEntryResult:
        res = await super().list_entrykeys(team, namespace)
        if res.entry_keys:
            for e in res.entry_keys:
                if not e.entry_key.startswith("_"):
                    get_res = await super().get(team, namespace, e.entry_key)
                    e.entry_key = json.loads(get_res.entry_value)[self.KEY_KEY]
        return res


def bytes_to_str(x):
    return b64encode(x).decode("utf-8")


def str_to_bytes(x):
    return b64decode(x.encode("utf-8"))


class RentalMsg(Enum):
    ADD = "add"
    REMOVE = "remove"
    RESERVE = "reserve"
    UNRESERVE = "unreserve"
    LOOKUP = "lookup"
    LIST = "list"
    HELP = "help"


class RentalHandler:
    """
    RentalHandler handles commands sent via chat to use the team key-value store.

    RentalHandler listens to chat messages of the form:
    `!rental {reserve|unreserve} <tool> <YYYY-MM-DD>`
    `!rental {lookup|add|remove} <tool>`
    `!rental list` // lists all tools

    It expects properly formatted commands.

    RentalHandler uses a cache to keep track of the most recently fetched value and
    revision for each key. To handle concurrent updates, it attempts to update
    with the most recently fetched revision + 1; if it fails, it does a "get"
    and updates the cache, and asks the user to retry if they still want to
    do their update.

    RentalHandler also maintains a cache of the per-team per-namespace hmac secrets
    it has previously fetched (stored with the special entryKey "_secret"),
    which it uses to HMAC entryKeys. RentalHandler uses the SecretKeyKVStoreClient
    to store entryKeys' HMACs instead of the plaintext entryKeys.
   """

    MSG_PREFIX = "!rental"
    NAMESPACE = "rental"

    def __init__(self):
        # self.cache = {tool: {"revision": int, "info": {} or None}}
        self.cache: Dict[Any, Any] = {}

    def update_cache(
        self, tool: str, reservations: Union[None, Dict[str, str]], revision: int
    ):
        self.cache[tool] = {"info": reservations, "revision": revision}

    async def lookup(self, bot, team, tool) -> keybase1.KVGetResult:
        res = await bot.secret_kvstore.get(team, self.NAMESPACE, tool)
        info = json.loads(res.entry_value) if res.entry_value != "" else None
        self.update_cache(tool, info, res.revision)
        return res

    async def add(
        self, bot, team, tool
    ) -> Union[keybase1.KVPutResult, keybase1.KVGetResult]:
        info = {SecretKeyKVStoreClient.KEY_KEY: tool}
        expected_revision = 1
        if tool in self.cache:
            # if tool already exists, propagate existing info
            if self.cache[tool]["info"]:
                info = self.cache[tool]["info"]
            expected_revision = self.cache[tool]["revision"] + 1
        info_str = json.dumps(info) if type(info) is dict else ""
        try:
            res: keybase1.KVPutResult = await bot.secret_kvstore.put(
                team, self.NAMESPACE, tool, info_str, expected_revision
            )
            self.update_cache(tool, info, res.revision)
            return res  # successful put. return KVPUtResult
        except RevisionError:
            # refresh cached value
            curr_info = await self.lookup(bot, team, tool)
            return curr_info  # failed put. return KVGetResult.

    async def remove(
        self, bot, team, tool
    ) -> Union[keybase1.KVDeleteEntryResult, keybase1.KVGetResult, None]:
        expected_revision = 1
        if tool in self.cache:
            expected_revision = self.cache[tool]["revision"] + 1
        try:
            res: keybase1.KVDeleteEntryResult = await bot.secret_kvstore.delete(
                team, self.NAMESPACE, tool, expected_revision
            )
            self.update_cache(tool, None, res.revision)
            return res  # successful delete. return KVDeleteEntryResult
        except RevisionError:
            # refresh cached value
            curr_info = await self.lookup(bot, team, tool)
            return curr_info  # failed put. return KVGetResult.
        except DeleteNonExistentError:
            # refresh cached value
            curr_info = await self.lookup(bot, team, tool)
            return None  # was already deleted. return None.

    async def update_reservation(
        self, bot, team, user, tool, day, reserve=True
    ) -> Union[keybase1.KVPutResult, keybase1.KVGetResult]:
        # note: if you reserve or unreserve a not-added or deleted tool, it will add the tool
        info = {SecretKeyKVStoreClient.KEY_KEY: tool}
        expected_revision = 1
        if tool in self.cache:
            if self.cache[tool]["info"]:
                info = self.cache[tool]["info"].copy()
            expected_revision = self.cache[tool]["revision"] + 1
        if reserve:
            info[day] = user
        else:
            # unreserve
            info.pop(day, None)
        try:
            res: keybase1.KVPutResult = await bot.secret_kvstore.put(
                team, self.NAMESPACE, tool, json.dumps(info), expected_revision
            )
            self.update_cache(tool, info, res.revision)
            return res  # successful put. return KVPUtResult
        except RevisionError:
            # refresh cached value
            curr_info = await self.lookup(bot, team, tool)
            return curr_info  # failed put. return KVGetResult.

    async def list_tools(self, bot, team) -> List[str]:
        res = await bot.secret_kvstore.list_entrykeys(team, self.NAMESPACE)
        keys = (
            [e.entry_key for e in res.entry_keys if not e.entry_key.startswith("_")]
            if res.entry_keys
            else []
        )
        return keys

    async def __call__(self, bot, event):
        members_type = event.msg.channel.members_type
        if not event.type == EventType.CHAT:
            return

        channel = event.msg.channel
        user = event.msg.sender.username

        # support teams and implicit self teams
        team = channel.name
        if members_type == "impteamnative" and channel.name == user:
            team = "{0},{0}".format(channel.name)

        msg = ""
        try:
            msg = event.msg.content.text.body.strip().split(" ")
        except AttributeError:
            return

        if len(msg) < 2 or msg[0] != self.MSG_PREFIX:
            return

        action = msg[1]
        if action == RentalMsg.HELP.value:
            return await self.handle_help(bot, channel, team, msg, action)
        if action == RentalMsg.LIST.value:
            return await self.handle_list(bot, channel, team, msg, action)
        if action == RentalMsg.LOOKUP.value:
            return await self.handle_lookup(bot, channel, team, msg, action)
        if action == RentalMsg.ADD.value:
            return await self.handle_add(bot, channel, team, msg, action)
        if action == RentalMsg.REMOVE.value:
            return await self.handle_remove(bot, channel, team, msg, action)
        if action == RentalMsg.RESERVE.value or action == RentalMsg.UNRESERVE.value:
            return await self.handle_reserve(bot, channel, team, msg, action, user)
        await bot.chat.send(channel, "invalid !rental command")
        return

    async def handle_help(self, bot, channel, team, msg, action):
        if len(msg) == 2:
            # !rental help
            send_msg = "Available commands:\
                    \n`!rental {reserve|unreserve} <tool> <YYYY-MM-DD>`\
                    \n`!rental {lookup|add|remove} <tool>`\
                    \n`!rental list` // lists all tools"
            await bot.chat.send(channel, send_msg)
            return

    async def handle_list(self, bot, channel, team, msg, action):
        if len(msg) == 2:
            # !rental list
            send_msg = await self.list_tools(bot, team)
            await bot.chat.send(channel, str(send_msg))
            return

    async def handle_lookup(self, bot, channel, team, msg, action):
        if len(msg) == 3:
            tool = msg[2]
            # !rental lookup <tool>
            res = await self.lookup(bot, team, tool)
            send_msg = (
                res.entry_value if len(res.entry_value) > 0 else "Entry does not exist."
            )
            await bot.chat.send(channel, send_msg)
            return

    async def handle_add(self, bot, channel, team, msg, action):
        if len(msg) == 3:
            # !rental add <tool>
            tool = msg[2]
            res = await self.add(bot, team, tool)
            if type(res) == keybase1.KVGetResult:
                send_msg = "Failed to write. Cache updated; try again to confirm write? Most recently fetched entry: {}.".format(
                    res
                )
                await bot.chat.send(channel, send_msg)
            elif type(res) == keybase1.KVPutResult:
                send_msg = "Successfully updated: {}".format(res)
                await bot.chat.send(channel, send_msg)
            return

    async def handle_remove(self, bot, channel, team, msg, action):
        if len(msg) == 3:
            # !rental remove <tool>
            tool = msg[2]
            res = await self.remove(bot, team, tool)
            if type(res) == keybase1.KVGetResult:
                send_msg = "Failed to write. Cache updated; try again to confirm write? Most recently fetched entry: {}.".format(
                    res
                )
                await bot.chat.send(channel, send_msg)
            elif type(res) == keybase1.KVDeleteEntryResult:
                send_msg = "Successfully updated: {}".format(res)
                await bot.chat.send(channel, send_msg)
            elif res is None:
                send_msg = "Value already does not exist."
                await bot.chat.send(channel, send_msg)
            return

    async def handle_reserve(self, bot, channel, team, msg, action, user):
        if len(msg) == 4:
            # !rental {reserve|unreserve} <tool> <YYYY-MM-DD>
            tool, day = msg[2], msg[3]
            res = await self.update_reservation(
                bot, team, user, tool, day, reserve=(action == RentalMsg.RESERVE.value)
            )
            if type(res) == keybase1.KVGetResult:
                send_msg = "Failed to write. Cache updated; try again to confirm write? Most recently fetched entry: {}.".format(
                    res
                )
                await bot.chat.send(channel, send_msg)
            elif type(res) == keybase1.KVPutResult:
                send_msg = "Successfully updated: {}".format(res)
                await bot.chat.send(channel, send_msg)
            return


username = "yourbot"

bot = CachedBot(
    username=username, paperkey=os.environ["KEYBASE_PAPERKEY"], handler=RentalHandler()
)

asyncio.run(bot.start({}))
