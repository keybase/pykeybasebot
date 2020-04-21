#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# Keybase has added an encrypted key-value store intended to support
# security-conscious bot development with persistent state. It is a place to
# store small bits of data that are
#   (1) encrypted for a team or user (via the user's implicit self-team: e.g.
# alice,alice),
#   (2) persistent across logins
#   (3) fast and durable.
#
# It supports putting, getting, listing, and deleting. There is also concurrency
# support, but check out 5_secret_storage.py for that. A team has many
# namespaces, a namespace has many entryKeys, and an entryKey has one current
# entryValue. Namespaces and entryKeys are in cleartext, and the Keybase client
# service will encrypt and sign the entryValue on the way in (as well as
# decrypt and verify on the way out) so keybase servers cannot see it or forge
# it.
#
# This example shows how you can use KVStoreClient to interact with the team
# encrypted key-value store.
###################################

import asyncio
import logging
import sys

from pykeybasebot import Bot
from pykeybasebot.errors import DeleteNonExistentError, RevisionError

logging.basicConfig(level=logging.DEBUG)

if "win32" in sys.platform:
    # Windows specific event-loop policy
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy()  # type: ignore
    )


async def simple_user():
    def noop_handler(*args, **kwargs):
        pass

    bot = Bot(handler=noop_handler())

    namespace = "current-favorites"
    key = "Sam"

    # using the default team, which is yourself (your implicit self-team
    # "yourusername,yourusername")

    # get a non-existent entry
    res = await bot.kvstore.get(namespace, key)
    print("GET NON-EXISTENT: ", res)
    assert res.entry_value is None

    # put with default revision
    # note: if revision=None, the service does a get (to get
    # the latest revision number) then a put (with revision
    # number + 1); this operation is not atomic.
    value = "The Left Hand of Darkness"
    res = await bot.kvstore.put(namespace, key, value, revision=None)
    print("PUT: ", res)
    rev = res.revision

    # fail put
    try:
        res = await bot.kvstore.put(namespace, key, "Fahrenheit 451", revision=rev)
    except RevisionError as e:
        print("EXPECTING PUT FAIL: ", e)

    # list namespaces
    res = await bot.kvstore.list_namespaces()
    print("LIST NAMESPACES: ", res)
    assert len(res.namespaces) > 0

    # list entryKeys
    res = await bot.kvstore.list_entrykeys(namespace)
    print("LIST ENTRYKEYS: ", res)
    assert len(res.entry_keys) > 0

    # get
    res = await bot.kvstore.get(namespace, key)
    print("GET: ", res)
    assert res.entry_value == value

    # fail delete
    try:
        res = await bot.kvstore.delete(namespace, key, revision=rev + 2)
    except RevisionError as e:
        print("EXPECTING DELETE FAIL: ", e)

    # delete
    res = await bot.kvstore.delete(namespace, key, revision=rev + 1)
    print("DELETE: ", res)
    assert res.revision == rev + 1

    # fail delete
    try:
        res = await bot.kvstore.delete(namespace, key, revision=rev + 2)
    except DeleteNonExistentError as e:
        print("EXPECTING DELETE FAIL: ", e)

    # get
    res = await bot.kvstore.get(namespace, key)
    print("GET: ", res)
    assert res.entry_value is None


async def main():
    print("Starting 3_simple_storage example...")
    await simple_user()
    print("...3_simple_storage example is complete.")


asyncio.run(main())
