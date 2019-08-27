#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# This example shows using the bot framework to build non-bot functionality.
# Here, the currently logged in user will send a message to the channel and
# then react three times to it with emoji or non-emoji "reactions." This
# pattern is used sometimes in Keybase teams to build a makeshift poll.
# The reactions are also sent asynchronously.
###################################

import asyncio
import logging

from pykeybasebot import Bot

logging.basicConfig(level=logging.DEBUG)


async def make_a_poll():
    channel = {
        "name": "yourcompany.marketing",
        "topic_name": "lunchtalk",
        "members_type": "team",
    }

    def noop_handler(*args, **kwargs):
        pass

    bot = Bot(
        # you don't need to pass in a username or paperkey if you're already logged in
        handler=noop_handler
    )

    resp = await bot.chat.send(channel, "what are y'all feeling for lunch?")
    msg_id = resp["result"]["id"]

    await asyncio.gather(
        bot.chat.react(channel, msg_id, ":burrito:"),
        bot.chat.react(channel, msg_id, ":sandwich:"),
        bot.chat.react(channel, msg_id, "other"),
    )


asyncio.run(make_a_poll())
