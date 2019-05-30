import asyncio
import json
import os
import re
import subprocess
import shlex

from .cli import kblisten, kbsubmit
from .chat_client import ChatClient


class Bot:
    def __init__(self, handler, name=None, loop=None):
        self.handler = handler
        self.name = name
        self.loop = loop

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.handler.__class__.__name__}, name={self.name})>"

    async def start(self, listen_options):
        async for event in kblisten(listen_options):
            if self.loop is not None:
                self.loop.create_task(self.handler(self, event))
            else:
                asyncio.create_task(self.handler(self, event))

    async def submit(self, command, input_data=None, **opts):
        return await kbsubmit(command, input_data, **opts)

    @property
    def chat(self):
        return ChatClient(self)

    async def oneshot(self, username, paperkey):
        env_with_paperkey = os.environ.copy()
        env_with_paperkey['KEYBASE_PAPERKEY'] = paperkey
        oneshot_command = f"keybase oneshot -u {username}"
        return await self.submit(oneshot_command, env=env_with_paperkey)
