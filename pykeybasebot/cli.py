import asyncio
import logging
import json
import subprocess
import shlex

from .kbevent import KbEvent


KEYBASE_TIMEOUT_MS = 2000


class KeybaseNotConnectedError(Exception):
    pass

async def kblisten(keybase_cli, options, loop=None):
    command = shlex.split(keybase_cli) + ['chat', 'api-listen']
    if options.get('local'):
        command.append('--local')
    if options.get('hide-exploding'):
        command.append('--hide-exploding')
    if options.get('dev'):
        command.append('--dev')
    if options.get('wallet'):
        command.append('--wallet')
    if options.get('filter-channel'):
        command.append('--filter-channel')
        command.append(json.dumps(options['filter-channel']))
    if options.get('filter-channels'):
        command.append('--filter-channels')
        command.append(json.dumps(options['filter-channels']))

    logging.debug(f"executing command: {command}")
    process = await asyncio.create_subprocess_exec(
        *command,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
        loop=loop,
    )
    while True:
        line = await process.stdout.readline()
        if not line:
            # when the keybase service dies, `api-listen` will emit empty byte strings
            raise KeybaseNotConnectedError("the keybase service is probably not running")
        try:
            yield KbEvent.from_json(line.decode().strip())
        except json.decoder.JSONDecodeError:
            # The first few messages that come out aren't actually valid json.
            # They just describe the options you've selected for listening.
            # It would probably be better only to do this `pass` for a couple
            # seconds.
            pass


async def kbsubmit(keybase_cli, command, input_data=None, **kwargs):
    cmd_list = shlex.split(keybase_cli) + shlex.split(command)
    process = await asyncio.create_subprocess_exec(
        *cmd_list,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        **kwargs)
    stdout, stderr = await asyncio.wait_for(
        process.communicate(input_data),
        KEYBASE_TIMEOUT_MS/1000.0,
        loop=kwargs.get('loop')
    )

    if process.returncode != 0:
        logging.error(f'[{command!r} exited with {process.returncode}]')
        logging.error(stderr.decode())

    response = stdout.decode('utf-8')
    try:
        return json.loads(response)
    except json.decoder.JSONDecodeError:
        return response
