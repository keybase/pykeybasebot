#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# This example shows using the bot framework to build non-bot functionality.
# Here, the currently logged in user will send a message to the channel and
# then looping through rotating the message by moving the first character to
# the end, and editing the original message with the rotated message. This
# creates a scrolling or marquee effect.
###################################

import asyncio
import logging
import time

from pykeybasebot import Bot


logging.basicConfig(level=logging.DEBUG)

def rotate(message):
    """
    Returns a string with the first character of 'message' moved to the end
    """
    return f"{message[1:]}{message[0]}"

async def scrolling_message(message, before="", after=""):
    channel = {
        "name": "yourcompany.marketing",
        "topic_name": "lunchtalk",
        "members_type": "team",
    }

    def noop_handler(*args, **kwargs):
        pass

    bot = Bot(
        username="currentlyloggedinuser",
        # you don't need to pass in a paperkey if you're already logged in
        handler=noop_handler,
    )

    resp = await bot.chat.send(channel, message)
    msg_id = resp['result']['id']

    while True:
        message = rotate(message)
        await bot.chat.edit(channel, msg_id, f"{before}{message}{after}")
        time.sleep(0.5)


asyncio.run(
    scrolling_message(
        "There's pizza in the break room!",
        #before="--[ `",
        #after="` ]--"
    )
)
