#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# This bot listens in one channel and reacts to every text message.
###################################

import asyncio
import logging
import os

import pykeybasebot.types.chat1 as chat1
from pykeybasebot import Bot

logging.basicConfig(level=logging.DEBUG)


async def handler(bot, event):
    if event.msg.content.type_name != chat1.MessageTypeStrings.TEXT.value:
        return
    channel = event.msg.channel
    msg_id = event.msg.id
    await bot.chat.react(channel, msg_id, ":clap:")


listen_options = {"filter-channel": {"name": "nsmith9,nathunsmitty"}}

bot = Bot(username="nsmith9", paperkey=os.environ["KEYBASE_PAPERKEY"], handler=handler)
asyncio.run(bot.start(listen_options))
