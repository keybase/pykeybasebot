#!/usr/bin/env python3

import asyncio
import logging

from pykeybasebot import Bot


logging.basicConfig(level=logging.DEBUG)


async def make_a_poll():
    channel = {"name": "yourcompany.marketing", "topic_name": "lunchtalk", "members_type": "team"}

    def noop_handler(*args, **kwargs):
        pass

    bot = Bot(
        username="currentlyloggedinuser",
        # you don't need to pass in a paperkey if youre already logged in
        handler=noop_handler,
    )

    resp = await bot.chat.send(channel, "what are y'all feeling for lunch?")
    msg_id = resp['result']['id']

    await bot.chat.react(channel, msg_id, ":burrito:")
    await bot.chat.react(channel, msg_id, ":sandwich:")
    await bot.chat.react(channel, msg_id, "other")


asyncio.run(make_a_poll())
