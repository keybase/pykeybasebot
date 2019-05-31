#!/usr/bin/env python3

import asyncio
import logging
import os

from pykeybasebot import Bot


logging.basicConfig(level=logging.DEBUG)


class Handler:
    async def __call__(self, bot, event):
        print(event)

listen_options = {
    'local': True,
    'wallet': True,
    'dev': True,
    'hide-exploding': False,
    'filter_channel': None,
    'filter_channels': None,
}

bot = Bot(
    username="yourbot",
    paperkey=os.environ['KEYBASE_PAPERKEY'],
    handler=Handler(),
)
asyncio.run(bot.start(listen_options))
