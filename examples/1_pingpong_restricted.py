#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# This bot listens to two channels for a special text message. When
# it sees this message, it replies in the same channel with a response.
# This also shows sending and receiving unicode characters.
# 
# By using the conversation id (conv_id) instead of the channel we can let restricted bots reply.
# From a security and privacy perspective it might be wise to use restricted bots where possible (see https://keybase.io/docs/teams/design).
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


class Handler:
    async def __call__(self, bot, event):
        if event.msg.content.type_name != chat1.MessageTypeStrings.TEXT.value:
            return
        if event.msg.content.text.body == "🌴ping🌴":
            # Use the conversation id instead of the channel to reply
            conv_id = event.msg.conv_id
            await bot.chat.send(conv_id, "🍹PONG!🍹")


listen_options = {
    "filter-channels": [
        {"name": "yourbot,someoneelse"},
        {
            "name": "yourcompany.marketing",
            "topic_name": "lunchtalk",
            "members_type": "team",
        },
    ]
}

bot = Bot(
    username="yourbot", paperkey=os.environ["KEYBASE_PAPERKEY"], handler=Handler()
)

asyncio.run(bot.start(listen_options))
