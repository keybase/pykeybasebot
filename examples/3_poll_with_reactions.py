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
from pykeybasebot.types import chat1

logging.basicConfig(level=logging.DEBUG)


async def make_a_poll():
    channel = chat1.ChatChannel(
        name="nathunsmitty,nsmith9",
        # "topic_name": "lunchtalk",
        # "members_type": "team",
    )

    def noop_handler(*args, **kwargs):
        pass

    # you don't need to pass in a username or paperkey if you're already logged in
    bot = Bot(handler=noop_handler)

    result = await bot.chat.send(channel, "what are y'all feeling for lunch?")
    msg_id = result.message_id

    await asyncio.gather(
        bot.chat.react(channel, msg_id, ":burrito:"),
        bot.chat.react(channel, msg_id, ":sandwich:"),
        bot.chat.react(channel, msg_id, "other"),
    )


asyncio.run(make_a_poll())
