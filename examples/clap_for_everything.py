#!/usr/bin/env python3

import asyncio
import logging

from kbpybot import Bot, ContentType


logging.basicConfig(level=logging.DEBUG)


class Handler:
    async def __call__(self, bot, event):
        if event.msg.content.type != ContentType.TEXT:
            return
        channel = event.msg.channel
        msg_id = event.msg.id
        await bot.chat.react(channel.replyable_dict(), msg_id, ":clap:")

listen_options = {
    'filter-channel': '{"name":"yourbot,someoneelse"}'
}

bot = Bot(Handler())
asyncio.run(bot.start(listen_options))
