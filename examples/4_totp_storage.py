#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# Keybase has added an encrypted key-value store; see 3_simple_storage.py for
# more information.
#
# This example shows how you can build a simple TOTP bot that makes use of
# the team encrypted key-value store.
###################################

import asyncio
import json
import logging
import os
import sys
from enum import Enum

import pyotp  # type: ignore

from pykeybasebot import Bot, EventType

logging.basicConfig(level=logging.DEBUG)

if "win32" in sys.platform:
    # Windows specific event-loop policy
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy()  # type: ignore
    )


class TotpMsg(Enum):
    ADD = "add"
    REMOVE = "remove"
    NOW = "now"
    LIST = "list"
    HELP = "help"


class TotpHandler:
    """
    TotpHandler handles commands sent via chat and uses the team key-value store to
    provide TOTP client functionality.

    TotpHandler listens to chat messages of the form:

    `!totp add <issuer> <secret>`
    `!totp {now|remove} <issuer>`
    `!totp {list|help}`

    For each provisioned key, the handler stores in the namespace "totp" one
    row, with the key "<issuer>" and the json blob value "{"secret": <16 char base32
    secret>}".

    This Keybase bot can be used in place of MFA apps like Google Authenticator and Authy
    for login processes that require two-step verification. This bot uses the
    pyotp library, so it is also compatible with other MFA apps.

    A Keybase TOTP bot could be useful for logins where you're already using a strong
    password, but are required to also use TOTP. Or it could be perfect for adding
    replay attack resistance to the physical keypad lock protecting your team's ice
    cream freezer.... Note that depending on the login process and how you use this bot
    with your Keybase team setup, this bot may not be appropriate for threat models
    that require a physical "second factor" device.

    For more information on TOTP, see https://pyotp.readthedocs.io/en/latest/,
    https://tools.ietf.org/html/rfc6238.
    """

    MSG_PREFIX = "!totp"
    NAMESPACE = "totp"

    def __init__(self):
        self.handlers = {
            TotpMsg.HELP.value: self.handle_help,
            TotpMsg.LIST.value: self.handle_list,
            TotpMsg.ADD.value: self.handle_add,
            TotpMsg.REMOVE.value: self.handle_remove,
            TotpMsg.NOW.value: self.handle_now,
        }

    def to_json(self, secret):
        return {"secret": secret}

    async def add(self, bot, team, issuer, secret):
        val = json.dumps(self.to_json(secret))
        await bot.kvstore.put(team, self.NAMESPACE, issuer, val)

    async def remove(self, bot, team, issuer):
        # throws exception if nothing to delete
        await bot.kvstore.delete(team, self.NAMESPACE, issuer)

    async def list(self, bot, team):
        # returns all TOTP entryKeys (the issuers) in this team
        res = await bot.kvstore.list_entrykeys(team, self.NAMESPACE)
        if res.entry_keys:
            return [e.entry_key for e in res.entry_keys]
        else:
            return []

    async def now(self, bot, team, issuer):
        res = await bot.kvstore.get(team, self.NAMESPACE, issuer)
        if bot.kvstore.is_present(res):
            # if secret is present
            secret = json.loads(res.entry_value)["secret"]
            return pyotp.TOTP(secret).now()
        else:
            return None

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
        if action in self.handlers:
            return await self.handlers[action](bot, channel, team, msg, action)
        await bot.chat.send(channel, "invalid !totp command")
        return

    async def handle_help(self, bot, channel, team, msg, action):
        if len(msg) == 2:
            # chat: "!totp help"
            send_msg = "Available commands:\
                    \n`!totp add <issuer> <secret>`\
                    \n`!totp {now|remove} <issuer>`\
                    \n`!totp {list|help}`"
            await bot.chat.send(channel, send_msg)
            return

    async def handle_list(self, bot, channel, team, msg, action):
        if len(msg) == 2:
            # chat: "!totp list"
            ns = await self.list(bot, team)
            await bot.chat.send(channel, str(ns))
            return

    async def handle_now(self, bot, channel, team, msg, action):
        if len(msg) == 3:
            # chat: "!totp now <issuer>"
            issuer = msg[2]
            send_msg = "Error getting current TOTP for {}".format(issuer)
            code = await self.now(bot, team, issuer)
            if code:
                send_msg = "Current TOTP for {}: {}".format(issuer, code)
            await bot.chat.send(channel, send_msg)
            return

    async def handle_add(self, bot, channel, team, msg, action):
        if len(msg) == 4:
            issuer, secret = msg[2], msg[3]
            # chat: "!totp add <issuer> <secret>"
            send_msg = "Error adding TOTP for {0}".format(issuer)
            try:
                await self.add(bot, team, issuer, secret)
                send_msg = "TOTP added for {}".format(issuer)
            except Exception as e:
                print(e)
            finally:
                await bot.chat.send(channel, send_msg)
            return

    async def handle_remove(self, bot, channel, team, msg, action):
        if len(msg) == 3:
            issuer = msg[2]
            # chat: "!totp remove <issuer>"
            send_msg = "No keys to remove for {}".format(issuer)
            try:
                await self.remove(bot, team, issuer)
                send_msg = "Removed TOTP keys for {}".format(issuer)
            except Exception as e:
                print(e)
            finally:
                await bot.chat.send(channel, send_msg)
            return


username = "yourbot"

bot = Bot(
    username=username, paperkey=os.environ["KEYBASE_PAPERKEY"], handler=TotpHandler()
)

asyncio.run(bot.start({}))
