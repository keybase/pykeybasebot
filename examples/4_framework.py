#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# This example shows an opinionated chatbot framework built on top
# of pykeybasebot. The aim is to allow the most simple command and
# response behavior while also hiding async complexity. This is not
# necessarily the best way to achieve this aim, it's more intended
# to be illustrative of building custom frameworks (and to encourage
# you to try building one of your own).
###################################

import asyncio
import functools
import logging
import os
import sys

import pykeybasebot
from pykeybasebot.types import chat1

logging.basicConfig(level=logging.ERROR)

if "win32" in sys.platform:
    # Windows specific event-loop policy
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())


def force_async(fn):
    from concurrent.futures import ThreadPoolExecutor
    import asyncio

    pool = ThreadPoolExecutor()

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        future = pool.submit(fn, *args, **kwargs)
        return asyncio.wrap_future(future)

    return wrapper


class BasicBot:
    def __init__(self, botname, paperkey, channels):
        self.botname = botname
        self.paperkey = paperkey
        self.channels = channels
        self._commands = []
        self._bot = None

    def run(self):
        self._bot = pykeybasebot.Bot(
            username=self.botname, paperkey=self.paperkey, handler=self.command_handler
        )
        bot_channels = []
        for channel in self.channels:
            team, topic = channel.split("#")
            bot_channels.append(
                {"name": team, "topic_name": topic, "members_type": "team"}
            )
        listen_options = {"filter-channels": bot_channels}
        asyncio.run(self._bot.start(listen_options))

    def add_command(self, trigger_func, command_func):
        async_command = force_async(command_func)
        self._commands.append(
            {"trigger_func": trigger_func, "command_func": async_command}
        )

    def reply(self, event, message):
        channel = event.msg.channel.replyable_dict()  # format the channel for sending
        # make a new loop to run the async bot.chat.send method in what is currently
        # a synchronous context
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._bot.chat.send(channel, message))

    async def command_handler(self, bot, event):
        for possibility in self._commands:
            if possibility["trigger_func"](self, event):
                return await possibility["command_func"](self, event)


##############################
# a bot using the above framework
##############################

pingbot = BasicBot(
    botname="yourbot",
    paperkey=os.environ["KEYBASE_PAPERKEY"],
    channels=["nathunsmitty,yourbot"],
)


def is_a_ping(basic_bot, event):
    if event.msg.content.type_name != chat1.MessageTypeStrings.TEXT.value:
        return False
    return event.msg.content.text.body == "ping"


def say_pong(basic_bot, event):
    basic_bot.reply(event, "PONG!")


pingbot.add_command(is_a_ping, say_pong)
pingbot.run()
