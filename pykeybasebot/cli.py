import asyncio
import logging
import json
import subprocess
import shlex

from .kbevent import KbEvent


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
        try:
            logging.debug(f"unparsed incoming event: {line.decode().strip()}")
            yield KbEvent.from_json(line.decode().strip())
        except json.decoder.JSONDecodeError:
            pass


async def kbsubmit(keybase_cli, command, input_data=None, **kwargs):
    cmd_list = shlex.split(keybase_cli) + shlex.split(command)
    logging.debug(f"executing command: {cmd_list} with input {input_data}")
    process = await asyncio.create_subprocess_exec(
        *cmd_list,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        **kwargs)
    stdout, stderr = await process.communicate(input_data)

    if process.returncode != 0:
        logging.error(f'[{command!r} exited with {process.returncode}]')
        logging.error(stderr.decode())

    response = stdout.decode('utf-8')
    try:
        return json.loads(response)
    except json.decoder.JSONDecodeError:
        return response
