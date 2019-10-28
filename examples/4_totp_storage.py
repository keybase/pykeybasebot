#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# Keybase has added an encrypted key-value store; see 4_simple_storage.py for
# more information.
#
# This example shows how you can build a simple TOTP bot that makes use of
# the team encrypted key-value store, which we interact with using KVStoreClient.
#
# This example does minimal error handling and is not concurrency safe.
###################################

import asyncio
import json
import logging
import os
import sys
from enum import Enum

import pyotp

from pykeybasebot import Bot, EventType

logging.basicConfig(level=logging.DEBUG)

if "win32" in sys.platform:
    # Windows specific event-loop policy
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())


class TotpMsg(Enum):
    PROVISION = "provision"
    REPROVISION = "reprovision"
    REMOVE = "remove"
    NOW = "now"
    URI = "uri"
    LIST = "list"


class TotpHandler:
    """
    TotpHandler handles commands sent via chat and uses the team key-value store to
    provide TOTP client functionality.

    TotpHandler listens to chat messages of the form:

    `!totp {provision|reprovision|remove|now|uri} <issuer>` and
    `!totp list`

    For each provisioned key, the handler stores in the namespace "totp" one
    row, with the key "<issuer" and the json blob value "{"secret": <16 char base32
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

    def to_json(self, secret):
        return {"secret": secret}

    async def __provision(self, bot, team, issuer, force: bool = False):
        secret = pyotp.random_base32()
        val = json.dumps(self.to_json(secret))
        if not force:
            try:
                # throws exception if 1 is not the latest revision + 1
                await bot.kvstore.put(team, self.NAMESPACE, issuer, val, revision=1)
            except Exception as e:
                res = await bot.kvstore.get(team, self.NAMESPACE, issuer)
                if bot.kvstore.is_deleted(res):
                    # then TOTP for this issuer was previously provisioned but
                    # was deleted. insert as latest revision + 1
                    await bot.kvstore.put(team, self.NAMESPACE, issuer)
                else:
                    # then TOTP for this issuer was previously provisioned and
                    # might still be in use, so raise the exception
                    raise e
        else:
            # reprovisioning; "force" provisioning by inserting as latest revision + 1
            await bot.kvstore.put(team, self.NAMESPACE, issuer, val)
        return pyotp.TOTP(secret).provisioning_uri(team, issuer_name=issuer)

    async def __remove(self, bot, team, issuer):
        # throws exception if nothing to delete
        await bot.kvstore.delete(team, self.NAMESPACE, issuer)

    async def __list(self, bot, team):
        # returns all namespaces in this team; assumes that all namespaces are
        # used for storing TOTP credentials
        res = await bot.kvstore.list_entrykeys(team, self.NAMESPACE)
        if res.entry_keys:
            return [e.entry_key for e in res.entry_keys]
        else:
            return []

    async def __uri(self, bot, team, issuer):
        totp = await self.__totp(bot, team, issuer)
        return totp.provisioning_uri(team, issuer_name=issuer) if totp else None

    async def __now(self, bot, team, issuer):
        totp = await self.__totp(bot, team, issuer)
        return totp.now() if totp else None

    async def __totp(self, bot, team, issuer):
        res = await bot.kvstore.get(team, self.NAMESPACE, issuer)
        if bot.kvstore.is_present(res):
            # if secret is present
            secret = json.loads(res.entry_value)["secret"]
            return pyotp.TOTP(secret)
        else:
            return None

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
        if len(msg) == 2 and msg[0] == self.MSG_PREFIX and msg[1] == TotpMsg.LIST.value:
            # chat: "!totp list"
            ns = await self.__list(bot, team)
            await bot.chat.send(channel, str(ns))
            return

        if not (len(msg) == 3 and msg[0] == self.MSG_PREFIX):
            return

        action, issuer = msg[1], msg[2]
        if action == TotpMsg.PROVISION.value:
            # chat: "!totp provision <issuer>"
            send_msg = "Error provisioning TOTP for {0}. If this issuer was previously provisioned, confirm reprovisioning with command `totp {1} {0}`.".format(
                issuer, TotpMsg.REPROVISION.value
            )
            try:
                uri = await self.__provision(bot, team, issuer, force=False)
                send_msg = "TOTP provisioned for {}. provisioning_uri={}".format(
                    issuer, uri
                )
            except Exception as e:
                print(e)
            finally:
                await bot.chat.send(channel, send_msg)
            return
        if action == TotpMsg.REPROVISION.value:
            # chat: "!totp reprovision <issuer>"
            send_msg = "Error reprovisioning TOTP for {}".format(issuer)
            try:
                uri = await self.__provision(bot, team, issuer, force=True)
                send_msg = "TOTP reprovisioned for {}. provisioning_uri={}".format(
                    issuer, uri
                )
            except Exception as e:
                print(e)
            finally:
                await bot.chat.send(channel, send_msg)
            return
        if action == TotpMsg.NOW.value:
            # chat: "!totp now <issuer>"
            send_msg = "Error getting current TOTP for {}".format(issuer)
            code = await self.__now(bot, team, issuer)
            if code:
                send_msg = "Current TOTP for {}: {}".format(issuer, code)
            await bot.chat.send(channel, send_msg)
            return
        if action == TotpMsg.URI.value:
            # chat: "!totp uri <issuer>"
            send_msg = "Error getting provisioning_uri for {}".format(issuer)
            uri = await self.__uri(bot, team, issuer)
            if uri:
                send_msg = uri
            await bot.chat.send(channel, send_msg)
            return
        if action == TotpMsg.REMOVE.value:
            # chat: "!totp remove <issuer>"
            send_msg = "No keys to remove for {}".format(issuer)
            try:
                await self.__remove(bot, team, issuer)
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
