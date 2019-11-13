#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# This bot demos showing off the async features of the framework.
# With the lock set to `True`, it will only process one event at
# a time to completion. With the lock set to `False` it will schedule
# the events to be handled asynchronously.
# This bot also shows manual management of the python event loop.
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
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy()  # type: ignore
    )


async def alert(bot, wait_sec, channel):
    await asyncio.sleep(wait_sec)
    await bot.chat.send(channel, f"waited: {wait_sec} and now... ALERT!")


class Handler:
    def __init__(self, use_lock=False):
        self.use_lock = use_lock
        self.lock = asyncio.Lock()

    async def __call__(self, bot, event):
        if event.msg.content.type_name != chat1.MessageTypeStrings.TEXT.value:
            return
        channel = event.msg.channel
        if event.msg.content.text.body != "trigger":
            return
        # If you message 3 "trigger"s in rapid succession, the bot should
        # be done sending the alerts in ~5 seconds as opposed to 15 seconds.
        # BUT if you try this again with use_lock=True, it will stack the
        # requests and take the full 15 seconds.
        if self.use_lock:
            async with self.lock:
                await alert(bot, 5, channel)
        else:
            await alert(bot, 5, channel)


listen_options = {"filter-channel": {"name": "yourbot,someoneelse"}}

loop = asyncio.get_event_loop()

bot = Bot(
    username="yourbot",
    paperkey=os.environ["KEYBASE_PAPERKEY"],
    handler=Handler(use_lock=False),
    loop=loop,
)
loop.run_until_complete(bot.start(listen_options))
loop.close()
