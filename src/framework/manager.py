import asyncio

from framework.utils import worker
from framework.text import text
from fronius.inverter import inverter


async def workers():
    await asyncio.gather(
        worker(text('10x10', 5, 'abc')),
        worker(inverter('20x20', 30)),
    )


async def main():
    try:
        await asyncio.wait_for(workers(), timeout=120.0)
    except asyncio.TimeoutError:
        print('timeout!')


asyncio.run(main())
