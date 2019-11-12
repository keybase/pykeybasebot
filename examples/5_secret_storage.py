#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# Keybase has added an encrypted key-value store; see 3_simple_storage.py for
# more information.
#
# This example implements a simple bot to manage hackerspace tool rentals. It
# shows one way you can obfuscate entryKeys (which are not encrypted) by
# storing their HMACs, so that no one but your team (not even
# Keybase) can know about the names of all the cool tools you have; you can do
# something similar to hide namespaces.
#
# Additionally this example handles concurrent writes by using explicit revision
# numbers to prevent one user from unintentionally clobbering another user's
# rental updates.
# ###################################

import asyncio
import hmac
import json
import logging
import secrets
import sys
from base64 import b64decode, b64encode
from typing import Dict, List, Union

from pykeybasebot import Bot, KVStoreClient
from pykeybasebot.errors import DeleteNonExistentError, RevisionError
from pykeybasebot.types import keybase1

logging.basicConfig(level=logging.DEBUG)

if "win32" in sys.platform:
    # Windows specific event-loop policy
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy()  # type: ignore
    )


class CustomKVStoreBot(Bot):
    """
        Custom bot that has some stateful clients.
    """

    def __init__(self, *args, **kwargs):
        basic_client = KVStoreClient(self)
        secret_kvstore_client = SecretKeyKVStoreClient(basic_client)  # is stateful
        self._trying_secret_kvstore_client = TryingKVStoreClient(secret_kvstore_client)
        super().__init__(*args, **kwargs)

    @property
    def kvstore(self):
        return self._trying_secret_kvstore_client


class TryingKVStoreClient:
    """
    TryingKVStoreClient tries kvstore write actions with explicit revision numbers.
    If it fails to write, it does a "get" and returns the get result.
    """

    def __init__(self, client):
        self.kvstore = client

    async def put(
        self,
        team: str,
        namespace: str,
        entry_key: str,
        entry_value: Dict[str, str],
        revision: Union[int, None] = None,
    ) -> Union[keybase1.KVPutResult, keybase1.KVGetResult]:
        try:
            res: keybase1.KVPutResult = await self.kvstore.put(
                team, namespace, entry_key, entry_value, revision
            )
            return res  # successful put. return KVPutResult
        except RevisionError:
            get = await self.get(team, namespace, entry_key)
            return get  # failed put. return KVGetResult.

    async def delete(
        self,
        team: str,
        namespace: str,
        entry_key: str,
        revision: Union[int, None] = None,
    ) -> Union[keybase1.KVDeleteEntryResult, keybase1.KVGetResult]:
        try:
            res: keybase1.KVDeleteEntryResult = await self.kvstore.delete(
                team, namespace, entry_key, revision
            )
            return res  # successful delete. return KVDeleteEntryResult
        except (RevisionError, DeleteNonExistentError):
            get = await self.get(team, namespace, entry_key)
            return get  # failed put. return KVGetResult.
        return res

    async def get(
        self, team: str, namespace: str, entry_key: str
    ) -> keybase1.KVGetResult:
        res = await self.kvstore.get(team, namespace, entry_key)
        return res

    async def list_entrykeys(
        self, team: str, namespace: str
    ) -> keybase1.KVListEntryResult:
        res = await self.kvstore.list_entrykeys(team, namespace)
        return res


def bytes_to_str(x):
    return b64encode(x).decode("utf-8")


def str_to_bytes(x):
    return b64decode(x.encode("utf-8"))


class SecretKeyKVStoreClient:
    """
        A SecretKeyKVStoreClient that hides the entryKeys from Keybase servers.
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

    def __init__(self, kvstore_client):
        # secrets = {team: {namespace: secret}}
        self.secrets: Dict[str, Dict[str, bytes]] = {}
        self.kvstore: KVStoreClient = kvstore_client

    async def load_secret(self, team, namespace) -> bytes:
        if team not in self.secrets or namespace not in self.secrets[team]:
            secret = secrets.token_bytes(self.SECRET_NUM_BYTES)
            try:
                # we don't expect self.SECRET_KEY's revision > 0
                await self.kvstore.put(
                    team, namespace, self.SECRET_KEY, bytes_to_str(secret), revision=1
                )
            except RevisionError:
                res: keybase1.KVGetResult = await self.kvstore.get(
                    team, namespace, self.SECRET_KEY
                )
                secret = str_to_bytes(res.entry_value)
            if team not in self.secrets:
                self.secrets[team] = {}
            self.secrets[team][namespace] = secret
        return self.secrets[team][namespace]

    async def hmac_key(self, team, namespace, entry_key) -> str:
        secret = await self.load_secret(team, namespace)
        return hmac.new(secret, entry_key.encode("utf-8")).hexdigest()

    async def put(
        self,
        team: str,
        namespace: str,
        entry_key: str,
        entry_value: Dict[str, str],
        revision: Union[int, None] = None,
    ) -> keybase1.KVPutResult:
        entry_value[SecretKeyKVStoreClient.KEY_KEY] = entry_key
        h = await self.hmac_key(team, namespace, entry_key)
        res = await self.kvstore.put(
            team, namespace, h, json.dumps(entry_value), revision
        )
        res.entry_key = entry_key
        return res

    async def delete(
        self,
        team: str,
        namespace: str,
        entry_key: str,
        revision: Union[int, None] = None,
    ) -> keybase1.KVDeleteEntryResult:
        h = await self.hmac_key(team, namespace, entry_key)
        res = await self.kvstore.delete(team, namespace, h, revision)
        res.entry_key = entry_key
        return res

    async def get(
        self, team: str, namespace: str, entry_key: str
    ) -> keybase1.KVGetResult:
        h = await self.hmac_key(team, namespace, entry_key)
        res = await self.kvstore.get(team, namespace, h)
        res.entry_key = entry_key
        return res

    async def list_entrykeys(
        self, team: str, namespace: str
    ) -> keybase1.KVListEntryResult:
        res = await self.kvstore.list_entrykeys(team, namespace)
        if res.entry_keys:
            for e in res.entry_keys:
                if not e.entry_key.startswith("_"):
                    get_res = await self.kvstore.get(team, namespace, e.entry_key)
                    e.entry_key = json.loads(get_res.entry_value)[self.KEY_KEY]
        return res


class RentalBotClient:
    """
        Wraps a KVStoreClient to expose methods to handle tool rentals.
    """

    NAMESPACE = "rental"

    def __init__(self, bot):
        self.kvstore = bot.kvstore

    async def lookup(self, team, tool) -> keybase1.KVGetResult:
        res = await self.kvstore.get(team, self.NAMESPACE, tool)
        return res

    async def add(
        self, team, tool
    ) -> Union[keybase1.KVPutResult, keybase1.KVGetResult]:
        res = await self.lookup(team, tool)
        info = (
            json.loads(res.entry_value) if res.entry_value != "" else {}
        )  # if tool already exists, propagate existing info
        expected_revision = res.revision + 1
        res = await self.kvstore.put(
            team, self.NAMESPACE, tool, info, expected_revision
        )
        return res

    async def remove(
        self, team, tool
    ) -> Union[keybase1.KVDeleteEntryResult, keybase1.KVGetResult, None]:
        expected_revision = 1
        res = await self.lookup(team, tool)
        expected_revision = res.revision + 1
        res = await self.kvstore.delete(team, self.NAMESPACE, tool, expected_revision)
        return res

    async def reserve(
        self, team, user, tool, day
    ) -> Union[keybase1.KVPutResult, keybase1.KVGetResult]:
        """
        reserve a tool for a given day if that day is already not reserved.
        note: if you reserve a not-added or deleted tool, it will add the tool
        """
        res = await self.lookup(team, tool)
        info = json.loads(res.entry_value) if res.entry_value != "" else {}
        if day in info:
            return res  # failed to put because day is already reserved.
        else:
            info[day] = user
        expected_revision = res.revision + 1
        res = await self.kvstore.put(
            team, self.NAMESPACE, tool, info, expected_revision
        )
        return res

    async def unreserve(
        self, team, user, tool, day
    ) -> Union[keybase1.KVPutResult, keybase1.KVGetResult]:
        """
        unreserve a tool for a given day if that day is currently reserved by
        the given user.
        note: if you unreserve a not-added or deleted tool, it will not add the tool
        """
        res = await self.lookup(team, tool)
        info = json.loads(res.entry_value) if res.entry_value != "" else {}
        if (day not in info) or (day in info and info[day] != user):
            # failed to put because currently not reserved, or current reserver is not user
            return res
        expected_revision = res.revision + 1
        res = await self.kvstore.put(
            team, self.NAMESPACE, tool, info, expected_revision
        )
        return res

    async def list_tools(self, team) -> List[str]:
        res = await self.kvstore.list_entrykeys(team, self.NAMESPACE)
        keys = (
            [e.entry_key for e in res.entry_keys if not e.entry_key.startswith("_")]
            if res.entry_keys
            else []
        )
        return keys


async def basic_rental_users(bot, rental, team):
    user1 = "Jo"
    user2 = "Charlie"
    date1 = "2044-03-12"
    date2 = "2044-06-12"
    date3 = "2044-06-13"
    tool = "laz0rs"

    res = await rental.list_tools(team)
    print("LIST TOOLS: ", res)

    res = await rental.lookup(team, tool)
    print("LOOKUP: ", res)

    res = await rental.add(team, tool)
    print("ADD: ", res)
    assert type(res) == keybase1.KVPutResult

    res = await rental.remove(team, tool)
    print("REMOVE: ", res)
    assert type(res) == keybase1.KVDeleteEntryResult

    res = await rental.add(team, tool)
    print("ADD: ", res)
    assert type(res) == keybase1.KVPutResult

    res = await rental.reserve(team, user1, tool, date1)
    print("RESERVE: ", res)
    assert type(res) == keybase1.KVPutResult

    res = await rental.reserve(team, user1, tool, date1)
    print("EXPECTING RESERVE FAIL: ", res)
    assert type(res) == keybase1.KVGetResult

    res = await rental.reserve(team, user2, tool, date2)
    print("RESERVE: ", res)
    assert type(res) == keybase1.KVPutResult

    res = await rental.lookup(team, tool)
    print("LOOKUP: ", res)

    res = await rental.unreserve(team, user1, tool, date3)
    print("EXPECTING UNRESERVE FAIL: ", res)
    assert type(res) == keybase1.KVGetResult

    res = await rental.unreserve(team, user1, tool, date2)
    print("EXPECTING UNRESERVE FAIL: ", res)
    assert type(res) == keybase1.KVGetResult

    res = await rental.unreserve(team, user1, tool, date1)
    print("UNRESERVE: ", res)
    assert type(res) == keybase1.KVPutResult

    res = await rental.lookup(team, tool)
    print("LOOKUP: ", res)


async def concurrent_rental_users(bot, rental, team):
    tool = "time travel machine"

    async def concurrent_rental_user(user_id: int):
        date = "2044-10-0{}".format(user_id)
        user = "user{}".format(user_id)

        i = 0
        while True:
            # keep trying to reserve for user's unique date until successful
            res = await rental.reserve(team, user, tool, date)
            i += 1
            print("{}, attempt {}, TRY TO RESERVE: {}".format(user, i, res))
            if type(res) == keybase1.KVPutResult:
                # success
                return

    async def pre():
        while True:
            res = await rental.remove(team, tool)
            if type(res) == keybase1.KVDeleteEntryResult:
                print("REMOVE: {}".format(res))
                break

    async def post():
        # check that the tool has been reserved for all 5 unique dates
        res = await rental.lookup(team, tool)
        print("LOOKUP: {}".format(res))
        assert len(json.loads(res.entry_value)) == 6  # one key is "_key"

    await asyncio.wait_for(pre(), timeout=5.0)
    # have 5 users concurrently try to reserve the same tool for 5 unique dates
    await asyncio.gather(
        concurrent_rental_user(1),
        concurrent_rental_user(2),
        concurrent_rental_user(3),
        concurrent_rental_user(4),
        concurrent_rental_user(5),
    )
    await post()


async def main():
    print("Starting 5_secret_storage example...")

    team = "yourhackerspace"

    def noop_handler(*args, **kwargs):
        pass

    bot = CustomKVStoreBot(handler=noop_handler(), keybase="/home/user/keybase")
    rental = RentalBotClient(bot)

    print("...basic rental actions...")
    await basic_rental_users(bot, rental, team)

    print("...multiple users try to reserve...")
    await concurrent_rental_users(bot, rental, team)

    print("...5_secret_storage example is complete.")


asyncio.run(main())
