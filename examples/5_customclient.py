#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# Listens to messages it sends and deletes them to illustrate extending the
# ChatClient for any Keybase API method.
###################################

import asyncio
import logging
import os
import sys

import pykeybasebot.types.chat1 as chat1
from pykeybasebot import Bot, ChatClient

logging.basicConfig(level=logging.DEBUG)

if "win32" in sys.platform:
    # Windows specific event-loop policy
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy()  # type: ignore
    )


class CustomClient(ChatClient):
    async def delete(
        self, channel: chat1.ChatChannel, message_id: int
    ) -> chat1.SendRes:
        await self.bot.ensure_initialized()
        res = await self.execute(
            {
                "method": "delete",
                "params": {
                    "options": {"channel": channel.to_dict(), "message_id": message_id}
                },
            }
        )
        return chat1.SendRes.from_dict(res)


class CustomBot(Bot):
    @property
    def chat(self):
        return CustomClient(self)


username = "yourbot"


class Handler:
    async def __call__(self, bot, event):
        if (
            event.msg.content.type_name != chat1.MessageTypeStrings.TEXT.value
            and event.msg.sender.username != username
        ):
            return
        if event.msg.content.text.body == "DELETEME":
            await bot.chat.delete(event.msg.channel, event.msg.id)


bot = CustomBot(
    username=username, paperkey=os.environ["KEYBASE_PAPERKEY"], handler=Handler()
)

asyncio.run(bot.start({}))
