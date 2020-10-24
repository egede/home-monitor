import matplotlib
import time
import asyncio


# https://stackoverflow.com/a/37999370
def move_figure(f, x, y):
    """Move figure's upper left corner to pixel (x, y)"""
    backend = matplotlib.get_backend()
    if backend == 'TkAgg':
        f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
    elif backend == 'WXAgg':
        f.canvas.manager.window.SetPosition((x, y))
    else:
        # This works for QT and GTK
        # You can also use window.setGeometry
        f.canvas.manager.window.move(x, y)


async def worker(widget):
    sleep = widget.updateinterval
    start = time.monotonic()
    while True:
        widget.display('X')
        passed = time.monotonic() - start
        sleeptime = -passed % sleep
        await asyncio.sleep(sleeptime)



# if __name__ == '__main__':

#     import matplotlib.pyplot as plt

#     f, ax = plt.subplots()
#     move_figure(f, 500, 300)
#     plt.show()
