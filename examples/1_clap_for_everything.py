#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# This bot listens in one channel and reacts to every text message.
###################################

import asyncio
import logging
import os
import sys

import pykeybasebot.types.chat1 as chat1
from pykeybasebot import Bot

logging.basicConfig(level=logging.DEBUG)

if "win32" in sys.platform:
    # Windows specific event-loop policy
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())


async def handler(bot, event):
    if event.msg.content.type_name != chat1.MessageTypeStrings.TEXT.value:
        return
    channel = event.msg.channel
    msg_id = event.msg.id
    await bot.chat.react(channel, msg_id, ":clap:")


listen_options = {"filter-channel": {"name": "yourbot,someoneelse"}}

bot = Bot(username="yourbot", paperkey=os.environ["KEYBASE_PAPERKEY"], handler=handler)

asyncio.run(bot.start(listen_options))
