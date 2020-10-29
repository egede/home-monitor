import asyncio

from guizero import App
from threading import Thread

from framework.utils import worker
from framework.text import text
# from fronius.inverter import inverter


def start_background_loop(loop: asyncio.AbstractEventLoop) -> None:
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def workers(*widgets):
    await asyncio.gather(*widgets)


def main():

    loop = asyncio.new_event_loop()
    t = Thread(target=start_background_loop, args=(loop,), daemon=True)
    t.start()

    app = App(title="Home monitor")
    message = worker(text(app, '10x10', 5, 'abc'))

    task = asyncio.run_coroutine_threadsafe(workers(message), loop)

    app.display()

    task.cancel()


main()
