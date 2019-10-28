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
# It supports putting, getting, listing and deleting. There is also a concurrency
# primitive, but check out the other example for that. A team has many
# namespaces, a namespace has many entryKeys, and an entryKey has one current
# entryValue. Namespaces and entryKeys are in cleartext, and the Keybase client
# service will encrypt and sign the entryValue on the way in (as well as
# decrypt and verify on the way out) so keybase servers cannot see it or lie
# about it.
#
# This example shows how you can use KVStoreClient to interact with the team
# encrypted key-value store.
#
# This example propagates errors to the chat user and is not concurrency safe.
###################################

import asyncio
import logging
import os
import sys
from enum import Enum

from pykeybasebot import Bot, EventType

logging.basicConfig(level=logging.DEBUG)

if "win32" in sys.platform:
    # Windows specific event-loop policy
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())


class KVMsg(Enum):
    PUT = "put"
    GET = "get"
    DELETE = "delete"
    LIST = "list"


class KVHandler:
    """
    KVHandler handles commands sent via chat to use the team key-value store.

    KVHandler listens to chat messages of the form:
    `!storage put <namespace> <key> <value> (<revision>)`
    `!storage {get|delete} <namespace> <key>`
    `!storage list`
    `!storage list <namespace>`

    It expects properly formatted commands.
    """

    MSG_PREFIX = "!storage"

    async def __call__(self, bot, event):
        members_type = event.msg.channel.members_type
        if not (
            event.type == EventType.CHAT
            and (members_type == "team" or members_type == "impteamnative")
        ):
            return

        channel = event.msg.channel

        # support teams and implicit self teams
        team = (
            channel.name if members_type == "team" else "{0},{0}".format(channel.name)
        )

        msg = event.msg.content.text.body.split(" ")
        if msg[0] != self.MSG_PREFIX:
            return

        if len(msg) == 2 and msg[1] == KVMsg.LIST.value:
            # !storage list
            res = await bot.kvstore.list_namespaces(team)
            await bot.chat.send(channel, str(res))
            return
        if len(msg) == 3 and msg[1] == KVMsg.LIST.value:
            # !storage list <namespace>
            namespace = msg[2]
            res = await bot.kvstore.list_entrykeys(team, namespace)
            await bot.chat.send(channel, str(res))
            return
        if len(msg) == 4:
            (action, namespace, key) = (msg[1], msg[2], msg[3])
            if action == KVMsg.GET.value:
                # !storage get <namespace> <key>
                res = await bot.kvstore.get(team, namespace, key)
                await bot.chat.send(channel, str(res))
                return
            if action == KVMsg.DELETE.value:
                # !storage delete <namespace> <key>
                try:
                    res = await bot.kvstore.delete(team, namespace, key)
                    await bot.chat.send(channel, str(res))
                except Exception as e:
                    await bot.chat.send(channel, str(e))
                return
        if len(msg) == 5 or len(msg) == 6:
            # !storage put <namespace> <key> <value> (<revision>)
            (action, namespace, key, value) = (msg[1], msg[2], msg[3], msg[4])
            revision = int(msg[5]) if len(msg) == 6 else None
            if action == KVMsg.PUT.value:
                try:
                    res = await bot.kvstore.put(
                        team, namespace, key, value, revision=revision
                    )
                    await bot.chat.send(channel, str(res))
                except Exception as e:
                    await bot.chat.send(channel, str(e))
                return


username = "user3"  # "yourbot"

bot = Bot(
    username=username,
    paperkey=os.environ["KEYBASE_PAPERKEY"],
    handler=KVHandler(),
    keybase="/home/user/Documents/repos/go/src/github.com/keybase/client/go/keybase/keybase",
)

asyncio.run(bot.start({}))
