import asyncio
from functools import wraps
import logging
import os
import time

from .cli import kblisten, kbsubmit, KeybaseNotConnectedError
from .chat_client import ChatClient


RETRY_ATTEMPTS = 100
SLEEP_SECS_BETWEEEN_RETRIES = 1


def _with_reconnect_to_keybase(keybase_bot_start_function):
    # This decorator manages catching disconnect errors from the keybase service
    # and attempting to reconnect to it periodically. If the very first attempt
    # to connect fails, that error will be allowed to bubble up.
    @wraps(keybase_bot_start_function)
    async def wrapped_f(self, *args, **kwargs):
        attempts = RETRY_ATTEMPTS
        while True:
            try:
                await keybase_bot_start_function(self, *args, **kwargs)
            except KeybaseNotConnectedError:
                if self._initialized:
                    # this is the first caught error after it was previously working
                    attempts = 0
                    self._initialized = False
                    logging.info(f"RECONNECT: the keybase service has died or disappeared. attempting to reconnect {RETRY_ATTEMPTS} times...")
                attempts += 1
                if attempts > RETRY_ATTEMPTS:
                    # Retries exhausted or the bot hasn't initialized on its first attempt.
                    # Either way, reraise the caught exception.
                    raise
                logging.info(f"RECONNECT: sleeping {SLEEP_SECS_BETWEEEN_RETRIES} seconds...")
                time.sleep(SLEEP_SECS_BETWEEEN_RETRIES)
    return wrapped_f


class _botlifecycle:
    # This context manager ensures that the bot is initialized and torn down
    # around calls to listening for events.
    def __init__(self, bot, listen_options):
        self.bot = bot
        self.listen_options = listen_options

    async def __aenter__(self):
        await self.bot.ensure_initialized()
        return kblisten(self.bot.keybase_cli, self.listen_options, loop=self.bot.loop)

    async def __aexit__(self, *args):
        await self.bot.teardown()


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

    @_with_reconnect_to_keybase
    async def start(self, listen_options):
        # This is the main, expected entry point.
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
            if not isinstance(res, dict):
                logging.error("the result of `status --json` was not a parseable json object")
                raise KeybaseNotConnectedError(f"the keybase service is probably not running: {res}")
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
