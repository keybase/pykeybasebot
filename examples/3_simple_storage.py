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
import os
import sys
from enum import Enum

from pykeybasebot import Bot, EventType

logging.basicConfig(level=logging.DEBUG)

if "win32" in sys.platform:
    # Windows specific event-loop policy
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy()  # type: ignore
    )


class KVMsg(Enum):
    PUT = "put"
    GET = "get"
    DELETE = "delete"
    LIST = "list"
    HELP = "help"


class KVHandler:
    """
    KVHandler handles commands sent via chat to use the team key-value store.

    KVHandler listens to chat messages of the form:
    `!storage put <namespace> <key> <value> (<revision>)`
    `!storage get <namespace> <key>`
    `!storage delete <namespace> <key> (<revision>)`
    `!storage list`  // list namespaces
    `!storage list <namespace>`  // list entries in namespace
    """

    MSG_PREFIX = "!storage"

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
        if action == KVMsg.HELP.value:
            return await self.handle_help(bot, event, channel, team, msg, action)
        if action == KVMsg.LIST.value:
            return await self.handle_list(bot, event, channel, team, msg, action)
        if action == KVMsg.GET.value:
            return await self.handle_get(bot, event, channel, team, msg, action)
        if action == KVMsg.PUT.value:
            return await self.handle_put(bot, event, channel, team, msg, action)
        if action == KVMsg.DELETE.value:
            return await self.handle_delete(bot, event, channel, team, msg, action)
        await bot.chat.send(channel, "invalid !storage command")
        return

    async def handle_help(self, bot, event, channel, team, msg, action):
        if len(msg) == 2:
            # !storage help
            send_msg = "Available commands:\
                    \n`!storage put <namespace> <key> <value> (<revision>)`\
                    \n`!storage get <namespace> <key>`\
                    \n`!storage delete <namespace> <key> (<revision>)`\
                    \n`!storage list  // list namespaces`\
                    \n`!storage list <namespace>  // list entries in namespace`"
            await bot.chat.send(channel, send_msg)
            return

    async def handle_list(self, bot, event, channel, team, msg, action):
        if len(msg) == 2:
            # !storage list
            res = await bot.kvstore.list_namespaces(team)
            await bot.chat.send(channel, str(res))
            return
        if len(msg) == 3:
            # !storage list <namespace>
            namespace = msg[2]
            res = await bot.kvstore.list_entrykeys(team, namespace)
            await bot.chat.send(channel, str(res))
            return

    async def handle_get(self, bot, event, channel, team, msg, action):
        if len(msg) == 4:
            namespace, key = msg[2], msg[3]
            # !storage get <namespace> <key>
            res = await bot.kvstore.get(team, namespace, key)
            await bot.chat.send(channel, str(res))
            return

    async def handle_put(self, bot, event, channel, team, msg, action):
        if len(msg) == 5 or len(msg) == 6:
            # !storage put <namespace> <key> <value> (<revision>)
            namespace, key, value = msg[2], msg[3], msg[4]
            try:
                revision = int(msg[5]) if len(msg) == 6 else None
            except ValueError as e:
                await bot.chat.send(channel, str(e))
            try:
                # note: if revision=None, the server does a get (to get
                # the latest revision number) then a put (with revision
                # number + 1); this operation is not atomic.
                res = await bot.kvstore.put(
                    team, namespace, key, value, revision=revision
                )
                await bot.chat.send(channel, str(res))
            except Exception as e:
                await bot.chat.send(channel, str(e))
            return

    async def handle_delete(self, bot, event, channel, team, msg, action):
        if len(msg) == 4 or len(msg) == 5:
            # !storage delete <namespace> <key> (<revision>)
            namespace, key = msg[2], msg[3]
            try:
                revision = int(msg[4]) if len(msg) == 5 else None
            except ValueError as e:
                await bot.chat.send(channel, str(e))
            try:
                res = await bot.kvstore.delete(team, namespace, key, revision=revision)
                await bot.chat.send(channel, str(res))
            except Exception as e:
                await bot.chat.send(channel, str(e))
            return


username = "yourbot"

bot = Bot(
    username=username, paperkey=os.environ["KEYBASE_PAPERKEY"], handler=KVHandler()
)

asyncio.run(bot.start({}))
