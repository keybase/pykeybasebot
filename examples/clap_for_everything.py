#!/usr/bin/env python3

import asyncio
import logging

from pykeybasebot import Bot, ContentType


logging.basicConfig(level=logging.DEBUG)


async def handler(bot, event):
    if event.msg.content.type != ContentType.TEXT:
        return
    channel = event.msg.channel
    msg_id = event.msg.id
    await bot.chat.react(channel.replyable_dict(), msg_id, ":clap:")


listen_options = {
    'filter-channel': {"name":"yourbot,someoneelse"}
}

bot = Bot(
    username="yourbot",
    paperkey=os.environ['KEYBASE_PAPERKEY'],
    handler=handler,
)
asyncio.run(bot.start(listen_options))
