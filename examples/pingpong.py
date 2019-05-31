#!/usr/bin/env python3

import asyncio
import logging
import os

from pykeybasebot import Bot, ContentType


logging.basicConfig(level=logging.DEBUG)


class Handler:
    async def __call__(self, bot, event):
        if event.msg.content.type != ContentType.TEXT:
            return
        if event.msg.content.text.body == "ping":
            channel = event.msg.channel
            await bot.chat.send(channel.replyable_dict(), "PONG!")

listen_options = {
    'filter-channels': [
        {"name": "yourbot,someoneelse"},
        {"name": "yourcompany.marketing", "topic_name": "lunchtalk", "members_type": "team"}
    ]
}

bot = Bot(
    username="yourbot",
    paperkey=os.environ['KEYBASE_PAPERKEY'],
    handler=Handler(),
)
asyncio.run(bot.start(listen_options))
