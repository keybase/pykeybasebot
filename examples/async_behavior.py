#!/usr/bin/env python3

import asyncio
import logging

from pykeybasebot import Bot, ContentType


logging.basicConfig(level=logging.DEBUG)


async def alert(bot, wait_sec, channel):
    await asyncio.sleep(wait_sec)
    await bot.chat.send(channel.replyable_dict(), f"waited: {wait_sec} and now... ALERT!")


class Handler:
    def __init__(self, use_lock=False):
        self.use_lock = use_lock
        self.lock = asyncio.Lock()

    async def __call__(self, bot, event):
        if event.msg.content.type != ContentType.TEXT:
            return
        channel = event.msg.channel
        if event.msg.content.text.body != "trigger":
            return
        # If you message 3 "trigger"s in rapid succession, the bot should
        # be done sending the alerts in ~5 seconds as opposed to 15 seconds.
        # BUT if you try this again with use_lock=True, it will stack the
        # requests and take the full 15 seconds.
        if self.use_lock:
            async with self.lock:
                await alert(bot, 5, channel)
        else:
            await alert(bot, 5, channel)


listen_options = {
    'filter-channel': '{"name":"yourbot,someoneelse"}'
}

loop = asyncio.get_event_loop()
bot = Bot(
    username="yourbot",
    handler=Handler(use_lock=False),
)
loop.run_until_complete(bot.start(listen_options))
loop.close()
