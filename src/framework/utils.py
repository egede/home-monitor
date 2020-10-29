import time
import asyncio

async def worker(widget):
    sleep = widget.updateinterval
    start = time.monotonic()
    while True:
        widget.update()
        passed = time.monotonic() - start
        sleeptime = -passed % sleep
        await asyncio.sleep(sleeptime)
