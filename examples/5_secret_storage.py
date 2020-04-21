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
#
# Here we've stored the HMAC secret and other entries in the team's kvstore;
# you could also store the entries in the bot's own kvstore (the default team).
#
# TODO: this is currently not working exactly right. sorry.
# ###################################

import asyncio
import hmac
import json
import logging
import secrets
import sys
from base64 import b64decode, b64encode
from typing import Dict, List, Tuple, Union

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
        namespace: str,
        entry_key: str,
        entry_value: Dict[str, str],
        team: str,
        revision: Union[int, None] = None,
    ) -> Union[keybase1.KVPutResult, keybase1.KVGetResult]:
        try:
            res: keybase1.KVPutResult = await self.kvstore.put(
                namespace, entry_key, entry_value, team=team, revision=revision
            )
            return res  # successful put. return KVPutResult
        except RevisionError:
            get = await self.get(team, namespace, entry_key)
            return get  # failed put. return KVGetResult.

    async def delete(
        self,
        namespace: str,
        entry_key: str,
        team: str,
        revision: Union[int, None] = None,
    ) -> Union[keybase1.KVDeleteEntryResult, keybase1.KVGetResult]:
        try:
            res: keybase1.KVDeleteEntryResult = await self.kvstore.delete(
                namespace=namespace, entry_key=entry_key, revision=revision, team=team
            )
            return res  # successful delete. return KVDeleteEntryResult
        except (RevisionError, DeleteNonExistentError):
            get = await self.get(team, namespace, entry_key)
            return get  # failed delete. return KVGetResult.
        return res

    async def get(
        self, namespace: str, entry_key: str, team: str
    ) -> keybase1.KVGetResult:
        res = await self.kvstore.get(namespace, entry_key, team)
        return res

    async def list_entrykeys(
        self, namespace: str, team: str
    ) -> keybase1.KVListEntryResult:
        res = await self.kvstore.list_entrykeys(namespace, team)
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
                    namespace,
                    self.SECRET_KEY,
                    bytes_to_str(secret),
                    revision=1,
                    team=team,
                )
            except RevisionError:
                res: keybase1.KVGetResult = await self.kvstore.get(
                    namespace, self.SECRET_KEY, team=team
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
            namespace, h, json.dumps(entry_value), revision=revision, team=team
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
        res = await self.kvstore.delete(namespace, h, revision=revision, team=team)
        res.entry_key = entry_key
        return res

    async def get(
        self, team: str, namespace: str, entry_key: str
    ) -> keybase1.KVGetResult:
        h = await self.hmac_key(team, namespace, entry_key)
        res = await self.kvstore.get(namespace, h, team=team)
        res.entry_key = entry_key
        return res

    async def list_entrykeys(
        self, team: str, namespace: str
    ) -> keybase1.KVListEntryResult:
        res = await self.kvstore.list_entrykeys(namespace, team=team)
        if res.entry_keys:
            res.entry_keys = [
                e for e in res.entry_keys if not e.entry_key.startswith("_")
            ]
            for e in res.entry_keys:
                get_res = await self.kvstore.get(namespace, e.entry_key, team=team)
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

    async def add(self, team, tool) -> Tuple[bool, Union[keybase1.KVGetResult, None]]:
        """
            returns tuple
                (whether action is successful,
                most recent get result if applicable)
        """
        res = await self.lookup(team, tool)
        if res.entry_value is not None:
            return (True, res)  # if tool already exists, return get
        expected_revision = res.revision + 1
        res = await self.kvstore.put(team, self.NAMESPACE, tool, {}, expected_revision)
        if type(res) == keybase1.KVGetResult:
            return (False, res)
        else:
            return (True, None)

    async def remove(
        self, team, tool
    ) -> Tuple[bool, Union[keybase1.KVGetResult, None]]:
        """
            returns tuple
                (whether action is successful,
                most recent get result if applicable)
        """
        res = await self.lookup(team, tool)
        if res.entry_value is not None:
            return (True, res)  # if tool already doesn't exist, return get
        expected_revision = res.revision + 1
        res = await self.kvstore.delete(
            namespace=self.NAMESPACE,
            entry_key=tool,
            revision=expected_revision,
            team=team,
        )
        if type(res) == keybase1.KVGetResult:
            return (False, res)
        else:
            return (True, None)

    async def reserve(
        self, team, user, tool, day
    ) -> Tuple[bool, Union[keybase1.KVGetResult, None]]:
        """
        reserve a tool for a given day if that day is already not reserved.
        note: if you reserve a not-added or deleted tool, it will add the tool

        returns tuple
                (whether action is successful,
                most recent get result if applicable)
        """
        res = await self.lookup(team, tool)
        info = json.loads(res.entry_value) if res.entry_value is not None else {}
        if day in info:
            return (False, res)  # failed to put because day is already reserved.
        else:
            info[day] = user
        expected_revision = res.revision + 1
        res = await self.kvstore.put(
            self.NAMESPACE, tool, info, revision=expected_revision, team=team
        )
        if type(res) == keybase1.KVGetResult:
            return (False, res)
        else:
            return (True, None)

    async def unreserve(
        self, team, user, tool, day
    ) -> Tuple[bool, Union[keybase1.KVGetResult, None]]:
        """
        unreserve a tool for a given day if that day is currently reserved by
        the given user.
        note: if you unreserve a not-added or deleted tool, it will not add the tool

        returns tuple
                (whether action is successful,
                most recent get result if applicable)
        """
        res = await self.lookup(team, tool)
        info = json.loads(res.entry_value) if res.entry_value is not None else {}
        if day not in info:
            # a noop because currently not reserved
            return (True, res)
        if day in info and info[day] != user:
            # failed to put because current reserver is not user
            return (False, res)

        info.pop(day)
        expected_revision = res.revision + 1
        res = await self.kvstore.put(
            self.NAMESPACE, tool, info, revision=expected_revision, team=team
        )
        if type(res) == keybase1.KVGetResult:
            return (False, res)
        else:
            return (True, None)

    async def list_tools(self, team) -> List[str]:
        res = await self.kvstore.list_entrykeys(self.NAMESPACE, team=team)
        keys = [e.entry_key for e in res.entry_keys] if res.entry_keys else []
        return keys


async def basic_rental_users(rental, team):
    user1 = "Jo"
    user2 = "Charlie"
    date1 = "2044-03-12"
    date2 = "2044-06-12"
    date3 = "2044-06-13"
    tool = "laz0rs"

    (ok, res) = await rental.remove(team, tool)
    print("REMOVE: ", ok, res)
    assert ok

    res = await rental.list_tools(team)
    print("LIST TOOLS: ", res)

    res = await rental.lookup(team, tool)
    print("LOOKUP: ", res)

    (ok, res) = await rental.add(team, tool)
    print("ADD: ", ok, res)
    assert ok

    (ok, res) = await rental.remove(team, tool)
    print("REMOVE: ", ok, res)
    assert ok

    (ok, res) = await rental.add(team, tool)
    print("ADD: ", ok, res)
    assert ok

    (ok, res) = await rental.reserve(team, user1, tool, date1)
    print("RESERVE: ", ok, res)
    assert ok

    (ok, res) = await rental.reserve(team, user1, tool, date1)
    print("EXPECTING RESERVE FAIL: ", ok, res)
    assert not ok

    (ok, res) = await rental.reserve(team, user2, tool, date2)
    print("RESERVE: ", ok, res)
    assert ok

    res = await rental.lookup(team, tool)
    print("LOOKUP: ", res)

    (ok, res) = await rental.unreserve(team, user1, tool, date3)
    print("UNRESERVE: ", ok, res)
    assert ok

    (ok, res) = await rental.unreserve(team, user1, tool, date2)
    print("EXPECTING UNRESERVE FAIL: ", ok, res)
    assert not ok

    (ok, res) = await rental.unreserve(team, user1, tool, date1)
    print("UNRESERVE: ", ok, res)
    assert ok

    res = await rental.lookup(team, tool)
    print("LOOKUP: ", res)
    info = json.loads(res.entry_value)
    assert len(info) == 2
    assert date2 in info
    assert SecretKeyKVStoreClient.KEY_KEY in info


async def concurrent_rental_users(bot, rental, team):
    tool = "time travel machine"

    async def concurrent_rental_user(user_id: int):
        date = "2044-10-0{}".format(user_id)
        user = "user{}".format(user_id)

        i = 0
        while True:
            # keep trying to reserve for user's unique date until successful
            (ok, res) = await rental.reserve(team, user, tool, date)
            i += 1
            print("{}, attempt {}, TRY TO RESERVE: {}, {}".format(user, i, ok, res))
            if ok:
                # success
                return

    async def pre():
        while True:
            (ok, res) = await rental.remove(team, tool)
            if ok:
                print("REMOVE: ", ok, res)
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

    bot = CustomKVStoreBot(handler=noop_handler())
    rental = RentalBotClient(bot)

    print("...basic rental actions...")
    await basic_rental_users(rental, team)

    print("...multiple users try to reserve...")
    await concurrent_rental_users(bot, rental, team)

    print("...5_secret_storage example is complete.")


asyncio.run(main())
