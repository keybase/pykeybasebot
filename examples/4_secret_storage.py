#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# Keybase has added an encrypted key-value store; see 4_simple_storage.py for
# more information.
#
# This example implements a simple bot to manage hackerspace tool rentals. It
# shows one way you can easily obfuscate entryKeys (which are by default
# not encrypted) so that no one but your team (not even Keybase) can know about
# the names of all the cool tools you have; you can do something similar to
# hide namespaces. Additionally this example handles concurrent writes using a cache
# to prevent one user from unintentionally clobbering another user's rental updates.
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


class SecretKeyKVStoreClient:
    """
        Wrapper around KVStoreClient.
        Hmacs entryKeys by a per-team, per-namespace random secret.
    """

    KEY_KEY = "_key"

    def __init__(self, kvstore: KVStoreClient):
        self.kvstore = kvstore

    async def hmac_key(self, secret: bytes, key: str) -> str:
        return hmac.new(secret, key.encode("utf-8")).hexdigest()

    async def put(
        self,
        secret: bytes,
        team: str,
        namespace: str,
        entryKey: str,
        entryValue: str,
        revision: Union[int, None] = None,
    ) -> keybase1.KVPutResult:
        h = await self.hmac_key(secret, entryKey)
        res = await self.kvstore.put(team, namespace, h, entryValue, revision)
        res.entry_key = entryKey
        return res

    async def delete(
        self,
        secret: bytes,
        team: str,
        namespace: str,
        entryKey: str,
        revision: Union[int, None] = None,
    ) -> keybase1.KVDeleteEntryResult:
        h = await self.hmac_key(secret, entryKey)
        res = await self.kvstore.delete(team, namespace, h, revision)
        res.entry_key = h
        return res

    async def get(
        self, secret: bytes, team: str, namespace: str, entryKey: str
    ) -> keybase1.KVGetResult:
        h = await self.hmac_key(secret, entryKey)
        res = await self.kvstore.get(team, namespace, h)
        res.entry_key = h
        return res

    async def list_entrykeys(
        self, secret: bytes, team: str, namespace: str
    ) -> keybase1.KVListEntryResult:
        res = await self.kvstore.list_entrykeys(team, namespace)
        print(res.entry_keys)
        if res.entry_keys:
            for e in res.entry_keys:
                if not e.entry_key.startswith("_"):
                    get_res = await self.kvstore.get(team, namespace, e.entry_key)
                    e.entry_key = json.loads(get_res.entry_value)[
                        self.KEY_KEY
                    ]  # modify
        print("list_entrykeys: ", res)
        return res


class RentalHandler:
    """
    RentalHandler handles commands sent via chat to use the team key-value store.

    RentalHandler listens to chat messages of the form:
    `!rental {reserve|unreserve} <tool> <YYYY-MM-DD>`
    `!rental {lookup|add|remove} <tool>`
    `!rental list` // lists all tools

    It expects properly formatted commands.

    It uses a cache to handle concurrent users.
    It maintains a cache of the hmac secrets it has previously fetched (stored
    with the special entryKey "_secret", and stores the hmac of the entryKey
    instead of the plaintext entryKey.
   """

    MSG_PREFIX = "!rental"
    NAMESPACE = "rental"
    SECRET_NUM_BYTES = 32
    SECRET_KEY = "_secret"

    def __init__(self):
        # cache = {tool: {"revision": int, "info": {} or None}}
        self.cache: Dict[Any, Any] = {}
        self.secrets: Dict[str, Dict[str, bytes]] = {}  # {team: {namespace: secret}}

    async def load_secret(self, bot, team, namespace):
        print("load box box: ", self.secrets)
        if team not in self.secrets or namespace not in self.secrets[team]:
            secret = secrets.token_bytes(self.SECRET_NUM_BYTES)
            try:
                # we don't expect self.SECRET_KEY's revision > 0
                res: keybase1.KVPutResult = await bot.kvstore.put(
                    team, namespace, self.SECRET_KEY, bytes_to_str(secret), revision=1
                )
                print("PUT RESULT: ", res)
            except RevisionError:
                res = await bot.kvstore.get(team, namespace, self.SECRET_KEY)
                secret = str_to_bytes(res.entry_value)
                print(">>>>gotten key: ", secret)
            if team not in self.secrets:
                self.secrets[team] = {}
            self.secrets[team][namespace] = secret
        print(">>>>>>>>>>>>>>>>>>")
        print(self.secrets)
        return self.secrets[team][namespace]

    def update_cache(
        self, tool: str, reservations: Union[None, Dict[str, str]], revision: int
    ):
        self.cache[tool] = {"info": reservations, "revision": revision}
        print("CACHE: ", self.cache)

    async def lookup(
        self, bot, team, tool, secret: Union[bytes, None]
    ) -> keybase1.KVGetResult:
        print("TOOL :   ", tool)
        if secret is None:
            secret = await self.load_secret(bot, team, self.NAMESPACE)
        res = await SecretKeyKVStoreClient(bot.kvstore).get(
            secret, team, self.NAMESPACE, tool
        )
        info = json.loads(res.entry_value) if res.entry_value != "" else None
        self.update_cache(tool, info, res.revision)
        return res

    async def add(
        self, bot, team, tool
    ) -> Union[keybase1.KVPutResult, keybase1.KVGetResult]:
        secret = await self.load_secret(bot, team, self.NAMESPACE)
        info = {SecretKeyKVStoreClient.KEY_KEY: tool}
        expected_revision = 1
        if tool in self.cache:
            # if tool already exists, propagate existing info
            if self.cache[tool]["info"] and type(self.cache[tool]["info"]) is dict:
                info = self.cache[tool]["info"]
            expected_revision = self.cache[tool]["revision"] + 1
        info_str = json.dumps(info) if type(info) is dict else ""
        try:
            res: keybase1.KVPutResult = await SecretKeyKVStoreClient(bot.kvstore).put(
                secret, team, self.NAMESPACE, tool, info_str, expected_revision
            )
            self.update_cache(tool, info, res.revision)
            return res  # successful put. return KVPUtResult
        except RevisionError:
            # refresh cached value
            curr_info = await self.lookup(bot, team, tool, secret=secret)
            return curr_info  # failed put. return KVGetResult.

    async def remove(
        self, bot, team, tool
    ) -> Union[keybase1.KVDeleteEntryResult, keybase1.KVGetResult, None]:
        secret = await self.load_secret(bot, team, self.NAMESPACE)
        expected_revision = 1
        if tool in self.cache:
            expected_revision = self.cache[tool]["revision"] + 1
        try:
            res: keybase1.KVDeleteEntryResult = await SecretKeyKVStoreClient(
                bot.kvstore
            ).delete(secret, team, self.NAMESPACE, tool, expected_revision)
            self.update_cache(tool, None, res.revision)
            return res  # successful delete. return KVDeleteEntryResult
        except RevisionError:
            # refresh cached value
            curr_info = await self.lookup(bot, team, tool, secret=secret)
            return curr_info  # failed put. return KVGetResult.
        except DeleteNonExistentError:
            # refresh cached value
            curr_info = await self.lookup(bot, team, tool, secret=secret)
            return None  # was already deleted. return None.

    async def update_reservation(
        self, bot, team, user, tool, day, reserve=True
    ) -> Union[keybase1.KVPutResult, keybase1.KVGetResult]:
        # note: if you reserve or unreserve a not-added or deleted tool, it will add the tool
        secret = await self.load_secret(bot, team, self.NAMESPACE)
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
            info.pop(tool, None)
        try:
            res: keybase1.KVPutResult = await SecretKeyKVStoreClient(bot.kvstore).put(
                secret, team, self.NAMESPACE, tool, json.dumps(info), expected_revision
            )
            self.update_cache(tool, info, res.revision)
            return res  # successful put. return KVPUtResult
        except RevisionError:
            # refresh cached value
            curr_info = await self.lookup(bot, team, tool, secret=None)
            return curr_info  # failed put. return KVGetResult.

    async def list_tools(self, bot, team) -> List[str]:
        secret = await self.load_secret(bot, team, self.NAMESPACE)
        res = await SecretKeyKVStoreClient(bot.kvstore).list_entrykeys(
            secret, team, self.NAMESPACE
        )
        keys = (
            [e.entry_key for e in res.entry_keys if not e.entry_key.startswith("_")]
            if res.entry_keys
            else []
        )
        return keys

    async def __call__(self, bot, event):
        print("----")
        print(event)
        members_type = event.msg.channel.members_type
        if not (
            event.type == EventType.CHAT
            and (members_type == "team" or members_type == "impteamnative")
        ):
            return

        channel = event.msg.channel
        user = event.msg.sender.username

        # support teams and implicit self teams
        team = (
            channel.name if members_type == "team" else "{0},{0}".format(channel.name)
        )

        msg = event.msg.content.text.body.split(" ")
        print(">>>msg: ", msg)
        if msg[0] != self.MSG_PREFIX:
            return

        if len(msg) == 2:
            if msg[1] == RentalMsg.LIST.value:
                # !rental list
                send_msg = await self.list_tools(bot, team)
                await bot.chat.send(channel, str(send_msg))
                return
            if msg[1] == RentalMsg.HELP.value:
                # !rental help
                send_msg = "Available commands:\
                    \n`!rental {reserve|unreserve} <tool> <YYYY-MM-DD>`\
                    \n`!rental {lookup|add|remove} <tool>`\
                    \n`!rental list` // lists all tools"
                await bot.chat.send(channel, send_msg)
                return
        if len(msg) == 3:
            (action, tool) = (msg[1], msg[2])
            if action == RentalMsg.LOOKUP.value:
                # !rental lookup <tool>  // lists info for all not-past days that tool is reserved
                res = await self.lookup(bot, team, tool, None)
                send_msg = (
                    res.entry_value
                    if len(res.entry_value) > 0
                    else "Entry does not exist."
                )
                await bot.chat.send(channel, send_msg)
                return
            if action == RentalMsg.ADD.value:
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
            if action == RentalMsg.REMOVE.value:
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
        if len(msg) == 4 and (
            msg[1] == RentalMsg.RESERVE.value or msg[1] == RentalMsg.UNRESERVE.value
        ):
            (action, tool, day) = (msg[1], msg[2], msg[3])
            # !rental {reserve|unreserve} <tool> <YYYY-MM-DD>
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
        await bot.chat.send(channel, "invalid !rental command")
        return


username = "yourbot"

bot = Bot(
    username=username, paperkey=os.environ["KEYBASE_PAPERKEY"], handler=RentalHandler()
)

asyncio.run(bot.start({}))
