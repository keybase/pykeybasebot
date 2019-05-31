import asyncio
import json
import os
import re
import subprocess
import shlex

from .cli import kblisten, kbsubmit
from .chat_client import ChatClient


class Bot:
    def __init__(self, username, handler, loop=None, keybase=None, home_path=None, pid_file=None):
        self.username = username
        self.handler = handler
        self.keybase = keybase or 'keybase'
        self.loop = loop
        self.home_path = home_path
        self.pid_file = pid_file

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.handler.__class__.__name__}, username={self.username})>"

    async def start(self, listen_options):
        async for event in kblisten(self.keybase_cli, listen_options):
            if self.loop is not None:
                self.loop.create_task(self.handler(self, event))
            else:
                asyncio.create_task(self.handler(self, event))

    async def submit(self, command, input_data=None, **opts):
        return await kbsubmit(self.keybase_cli, command, input_data, **opts)

    @property
    def chat(self):
        return ChatClient(self)

    async def oneshot(self, paperkey):
        env_with_paperkey = os.environ.copy()
        env_with_paperkey['KEYBASE_PAPERKEY'] = paperkey
        oneshot_command = f"oneshot -u {self.username}"
        return await self.submit(oneshot_command, env=env_with_paperkey)

    @property
    def keybase_cli(self):
        command = self.keybase
        if self.home_path is not None:
            command += f" --home {self.home_path}"
        if self.pid_file is not None:
            command += f" --pid-file {self.pid_file}"
        return command
