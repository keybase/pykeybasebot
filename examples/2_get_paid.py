#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# This bot listens for completed payments. When it gets paid,
# it does something.
###################################

import asyncio
import logging
import os

from pykeybasebot import Bot, EventType, PaymentStatusStr


logging.basicConfig(level=logging.DEBUG)


DollarsPerLumen = 0.13


def parse_usd_amount(amount_description):
    # "20.1234 XLM" => 2.614
    amount_str, currency = amount_description.split()
    assert currency == "XLM"
    return float(amount_str) * DollarsPerLumen

class Handler:
    async def __call__(self, bot, event):
        if event.type != EventType.WALLET:
            return
        if event.notification.statusDescription != PaymentStatusStr.COMPLETED:
            return

        usd = parse_usd_amount(event.notification.amountDescription)
        sender = event.notification.fromUsername

        channel = {"name": f"{bot.name},{sender}"}
        message = "thank you so much for the ${0:.2f} :moneybag:".format(usd)
        await bot.chat.send(channel, message)


listen_options = {
    "wallet": True
}

bot = Bot(
    username="yourbot",
    paperkey=os.environ['KEYBASE_PAPERKEY'],
    handler=Handler(),
)
asyncio.run(bot.start(listen_options))
