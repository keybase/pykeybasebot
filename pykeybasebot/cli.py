import asyncio
import json
import logging
import shlex

from .kbevent import KbEvent

DEFAULT_TIMEOUT_MS = 10000


class KeybaseNotConnectedError(Exception):
    pass


async def kblisten(keybase_cli: str, options, loop=None):
    command = shlex.split(keybase_cli) + ["chat", "api-listen"]
    if options.get("local"):
        command.append("--local")
    if options.get("hide-exploding"):
        command.append("--hide-exploding")
    if options.get("dev"):
        command.append("--dev")
    if options.get("wallet"):
        command.append("--wallet")
    if options.get("filter-channel"):
        command.append("--filter-channel")
        command.append(json.dumps(options["filter-channel"]))
    if options.get("filter-channels"):
        command.append("--filter-channels")
        command.append(json.dumps(options["filter-channels"]))

    logging.debug(f"executing command: {command}")
    process = await asyncio.create_subprocess_exec(
        *command,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
        loop=loop,
    )
    while True:
        if not process.stdout:
            raise Exception("Process not initialized correctly")
        line = await process.stdout.readline()
        if not line:
            # when the keybase service dies, `api-listen` will emit empty byte strings
            raise KeybaseNotConnectedError(
                "the keybase service is probably not running"
            )
        decoded_line = line.decode().strip()
        try:
            yield KbEvent.from_json(decoded_line)
        except json.decoder.JSONDecodeError:
            logging.error(f"Unable to decode JSON output: {line}")
            pass


async def kbsubmit(
    keybase_cli: str, command: str, input_data=None, timeout_ms=None, **kwargs
):
    cmd_list = shlex.split(keybase_cli) + shlex.split(command)
    process = await asyncio.create_subprocess_exec(
        *cmd_list,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        **kwargs,
    )
    if timeout_ms is None:
        timeout_ms = DEFAULT_TIMEOUT_MS
    stdout, stderr = await asyncio.wait_for(
        process.communicate(input_data), timeout_ms / 1000.0, loop=kwargs.get("loop")
    )

    if process.returncode != 0:
        logging.error(f"[{command!r} exited with {process.returncode}]")
        logging.error(stderr.decode())

    response = stdout.decode("utf-8")
    try:
        parsed_response = json.loads(response)
        if "error" in parsed_response:
            raise Exception(parsed_response["error"])
        return parsed_response
    except json.decoder.JSONDecodeError:
        return response
