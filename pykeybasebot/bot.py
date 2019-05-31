import asyncio
import json
import logging
import os
import re
import subprocess
import shlex

from .cli import kblisten, kbsubmit
from .chat_client import ChatClient


class Bot:
    def __init__(self, username, handler, paperkey=None, loop=None, keybase=None, home_path=None, pid_file=None):
        self.username = username
        self.paperkey = paperkey
        self.handler = handler
        self.keybase = keybase or 'keybase'
        self.loop = loop
        self.home_path = home_path
        self.pid_file = pid_file
        self._initialized = False

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.handler.__class__.__name__}, username={self.username})>"

    async def start(self, listen_options):
        await self.must_be_initialized()
        async for event in kblisten(self.keybase_cli, listen_options):
            if self.loop is not None:
                self.loop.create_task(self.handler(self, event))
            else:
                asyncio.create_task(self.handler(self, event))

    async def submit(self, command, input_data=None, **opts):
        return await kbsubmit(self.keybase_cli, command, input_data, loop=self.loop, **opts)

    @property
    def keybase_cli(self):
        command = self.keybase
        if self.home_path is not None:
            command += f" --home {self.home_path}"
        if self.pid_file is not None:
            command += f" --pid-file {self.pid_file}"
        return command

    @property
    def chat(self):
        return ChatClient(self)

    async def must_be_initialized(self):
        if not await self.is_initialized():
            oneshot_res = await self.oneshot()
            if not await self.is_initialized():
                logging.error("failed to initialize using oneshot")
                logging.error(f"oneshot results: {oneshot_res}")
                raise "You must be logged in to do this. Calling `oneshot` with your paperkey failed."

    async def is_initialized(self):
        if not self._initialized:
            res = await self.submit('status --json')
            actual_username = res['Username']
            actual_logged_in = res['LoggedIn']
            self._initialized = (self.username == actual_username and actual_logged_in)
        return self._initialized

    async def oneshot(self):
        env_with_paperkey = os.environ.copy()
        env_with_paperkey['KEYBASE_PAPERKEY'] = self.paperkey
        oneshot_command = f"oneshot -u {self.username}"
        await self.submit(oneshot_command, env=env_with_paperkey)
