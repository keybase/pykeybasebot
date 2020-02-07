import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

import pytest
import yaml

from pykeybasebot import Bot, kbsubmit
from pykeybasebot.types import chat1


@pytest.fixture()
def config_location():
    app_dir = Path().absolute()
    return os.path.join(app_dir, "tests/acceptance/test_config.yaml")


@pytest.fixture()
def config(config_location):
    with open(config_location) as file:
        data = yaml.safe_load(file)
        return data


@pytest.fixture()
def channel(config):
    return chat1.ChatChannel(
        name=f"{config['bots']['alice']['username']},{config['bots']['bob']['username']}"
    )


@pytest.fixture()
def conv_id(config):
    return chat1.ConvIDStr(f"{config['teams']['acme']['conv_id']}")


def noop_handler(*args, **kwargs):
    pass


@pytest.fixture()
async def setup_bot(config):
    with tempfile.TemporaryDirectory() as tmpdir:
        kb_location = shutil.which("keybase").strip()
        kb_destination = f"{tmpdir}/keybase"
        shutil.copy(kb_location, kb_destination)

        args = [kb_destination, "--home", tmpdir, "service"]
        subprocess.Popen(args)
        # Give the service a second to start up
        time.sleep(2)

        bot = None

        def setup_bot_with_name(name):
            nonlocal bot
            bot = Bot(
                username=config["bots"][name]["username"],
                paperkey=config["bots"][name]["paperkey"],
                handler=noop_handler,
                home_path=tmpdir,
                keybase=kb_destination,
            )
            return bot

        yield setup_bot_with_name
        await bot.teardown()
        await kbsubmit(kb_destination, "ctl stop")


@pytest.mark.asyncio
async def test_list(setup_bot):
    bot = setup_bot("alice")
    conversations = await bot.chat.list()
    for conversation in conversations:
        assert type(conversation) is chat1.ConvSummary


@pytest.mark.asyncio
async def test_read(setup_bot, channel):
    bot = setup_bot("alice")
    messages = await bot.chat.read(channel)
    for message in messages:
        assert type(message) is chat1.MsgSummary


@pytest.mark.asyncio
async def test_read_conv_id(setup_bot, conv_id):
    bot = setup_bot("alice")
    messages = await bot.chat.read(conv_id)
    for message in messages:
        assert type(message) is chat1.MsgSummary
