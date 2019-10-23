import asyncio
import os
import shutil
import subprocess
import tempfile
import time

from pykeybasebot import Bot, kbsubmit
from pykeybasebot.types import chat1

import pytest
import yaml


def create_working_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        kb_location = shutil.which("keybase").strip()
        kb_destination = f"{tmpdir}/keybase"
        shutil.copy(kb_location, kb_destination)
        print(os.listdir(tmpdir))


@pytest.fixture()
def config():
    with open("tests/test_config.yaml") as f:
        data = yaml.safe_load(f)
        return data


@pytest.fixture()
def channel(config):
    return chat1.ChatChannel(
        name=f"{config['bots']['alice']['username']},{config['bots']['bob']['username']}"
    )


@pytest.fixture()
async def bot(config):
    with tempfile.TemporaryDirectory() as tmpdir:
        kb_location = shutil.which("keybase").strip()
        kb_destination = f"{tmpdir}/keybase"
        shutil.copy(kb_location, kb_destination)

        args = [kb_destination, "--home", tmpdir, "service"]
        subprocess.Popen(args)
        time.sleep(2)

        bot = Bot(
            username=config["bots"]["alice"]["username"],
            paperkey=config["bots"]["alice"]["paperkey"],
            handler=noop_handler,
            home_path=tmpdir,
            keybase=kb_destination,
        )
        yield bot
        await bot.teardown()
        await kbsubmit(kb_destination, "ctl stop")


def noop_handler(*args, **kwargs):
    pass


@pytest.mark.asyncio
async def test_list(bot):
    conversations = await bot.chat.list()
    for conversation in conversations:
        assert type(conversation) is chat1.ConvSummary


@pytest.mark.asyncio
async def test_read(bot, channel):
    messages = await bot.chat.read(channel)
    for message in messages:
        assert type(message) is chat1.MsgSummary
