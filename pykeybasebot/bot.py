import asyncio
import logging
import os

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
        async with _botlifecycle(self, listen_options) as events:
            async for event in events:
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

    async def ensure_initialized(self):
        if not await self._is_initialized():
            await self._initialize()

    async def _is_initialized(self):
        if not self._initialized:
            res = await self.submit('status --json')
            actual_username = res['Username']
            actual_logged_in = res['LoggedIn']
            self._initialized = (self.username == actual_username and actual_logged_in)
        return self._initialized

    async def _initialize(self):
        if await self._is_initialized():
            # already initialized. fine to bail.
            return
        # login as a `oneshot` device
        env_with_paperkey = os.environ.copy()
        env_with_paperkey['KEYBASE_PAPERKEY'] = self.paperkey
        oneshot_command = f"oneshot -u {self.username}"
        oneshot_result = await self.submit(oneshot_command, env=env_with_paperkey)
        logging.info(oneshot_result)
        if not await self._is_initialized():
            # raise an exception because we can't authenticate
            raise f"failed to initialize with oneshot {oneshot_res}"

    async def teardown(self):
        await self.submit("logout")


class _botlifecycle:
    # manage ensuring that the bot is initialized and torn down
    # around calls to listening for events.
    def __init__(self, bot, listen_options):
        self.bot = bot
        self.listen_options = listen_options

    async def __aenter__(self):
        await self.bot.ensure_initialized()
        return kblisten(self.bot.keybase_cli, self.listen_options, loop=self.bot.loop)

    async def __aexit__(self, *args):
        await self.bot.teardown()
