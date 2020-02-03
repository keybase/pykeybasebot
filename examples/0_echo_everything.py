#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# This bot listens to every channel and every
# available message type. It prints all parsed
# events to STDOUT. This is the simplest bot
# in the set of examples.
###################################

import asyncio
import logging
import os
import sys

from pykeybasebot import Bot

logging.basicConfig(level=logging.DEBUG)

if "win32" in sys.platform:
    # Windows specific event-loop policy
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy()  # type: ignore
    )


class Handler:
    async def __call__(self, bot, event):
        print(event)


listen_options = {
    "local": True,
    "wallet": True,
    "dev": True,
    "hide-exploding": False,
    "convs": True,
    "filter_channel": None,
    "filter_channels": None,
}

bot = Bot(
    username="yourbot", paperkey=os.environ["KEYBASE_PAPERKEY"], handler=Handler()
)

asyncio.run(bot.start(listen_options))
