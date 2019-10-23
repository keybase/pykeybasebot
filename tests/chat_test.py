import asyncio
import os
import shutil
import subprocess
import tempfile
import time

from pykeybasebot import Bot
from pykeybasebot.types import chat1

import pytest
import yaml


# read config
def read_config():
    with open("tests/test_config.yaml") as f:
        data = yaml.safe_load(f)
        return data


# create temp dir
def create_working_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        kb_location = shutil.which("keybase").strip()
        kb_destination = f"{tmpdir}/keybase"
        shutil.copy(kb_location, kb_destination)
        print(os.listdir(tmpdir))


# copy keybase to temp dir
# start service
# test
# stop service


def noop_handler(*args, **kwargs):
    pass


@pytest.mark.asyncio
async def test_list():
    # init bot
    config = read_config()
    tmpdir = tempfile.mkdtemp()
    kb_location = shutil.which("keybase").strip()
    kb_destination = f"{tmpdir}/keybase"
    shutil.copy(kb_location, kb_destination)

    args = [kb_destination, "--home", tmpdir, "service"]
    print(" ".join(args))
    subprocess.Popen(args)
    time.sleep(2)

    bot = Bot(
        username=config["bots"]["alice"]["username"],
        paperkey=config["bots"]["alice"]["paperkey"],
        handler=noop_handler,
        home_path=tmpdir,
        keybase=kb_destination,
    )

    conversations = await bot.chat.list()

    for conversation in conversations:
        assert type(conversation) is chat1.ConvSummary


@pytest.mark.asyncio
async def test_read():
    pass
