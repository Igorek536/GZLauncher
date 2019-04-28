"""
Async process executor

@author: Igorek536
@version: 1.0
@contact: igorek536.freecore@gmail.com
"""

import asyncio
import platform
import enum


class System(enum.Enum):
    Linux64 = 1
    Linux32 = 2
    Windows64 = 3
    Windows32 = 4
    Unsupported = 5


def get_os():
    result = System.Unsupported
    if platform.system() == "Linux":
        if platform.machine() == "x86_64":
            result = System.Linux64
        elif platform.machine() == "i386":
            result = System.Linux32
    elif platform.system() == "Windows":
        if platform.machine() == "x86_64":
            result = System.Windows64
        elif platform.machine() == "i386":
            result = System.Windows32
    return result


async def read_stream(stream, cb):
    while 1:
        line = await stream.readline()
        if line:
            cb(line)
        else:
            break


async def stream_subprocess(cmd, stdout_cb, stderr_cb, env):
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    await asyncio.wait([
        read_stream(proc.stdout, stdout_cb),
        read_stream(proc.stderr, stderr_cb)
    ])


def execute(cmd, stdout_cb, stderr_cb, env=None):
    result = -3
    if get_os() is not System.Unsupported:
        if cmd is not None:
            loop = asyncio.get_event_loop()
            try:
                result = loop.run_until_complete(
                    stream_subprocess(cmd, stdout_cb, stderr_cb, env))
                loop.close()
            except FileNotFoundError as a:
                print("OOOOOPS!", a)
        else:
            result = -1
    return result


if get_os() is System.Windows64 or get_os() is System.Windows32:
    asyncio.set_event_loop(asyncio.ProactorEventLoop())
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
