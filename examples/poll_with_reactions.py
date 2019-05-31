#!/usr/bin/env python3

import asyncio
import logging

from pykeybasebot import Bot


logging.basicConfig(level=logging.DEBUG)


async def make_a_poll():
    channel = {"name": "yourcompany.marketing", "topic_name": "lunchtalk", "members_type": "team"}
    paperkey = os.environ['KEYBASE_PAPERKEY']

    def noop_handler(*args, **kwargs):
        pass

    bot = Bot(
        username="yourbot",
        handler=noop_handler,
    )
    await bot.oneshot(paperkey)

    resp = await bot.chat.send(channel, "what are y'all feeling for lunch?")
    msg_id = resp['result']['id']

    await bot.chat.react(channel, msg_id, ":burrito:")
    await bot.chat.react(channel, msg_id, ":sandwich:")
    await bot.chat.react(channel, msg_id, "other")


asyncio.run(make_a_poll())
