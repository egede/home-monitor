import unittest
from unittest import mock

import asyncio
import time

from framework.utils import worker
from framework.utils import move_figure


class WorkerTestCase(unittest.TestCase):

    def test_worker(self):

        class dummy():

            def __init__(self):
                self.updateinterval = 1

            def display(self, arg):
                time.sleep(1)

        async def workers():
            await asyncio.gather(
                worker(dummy()),
                worker(dummy()),
            )

        async def main():
            await asyncio.wait_for(workers(), timeout=1.0)

        try:
            asyncio.run(main())
        except Exception:
            pass

    @mock.patch('framework.utils.matplotlib')
    def test_move_tkagg(self, mock_mpl):
        mock_mpl.get_backend.return_value = 'TkAgg'
        f = mock.Mock()
        move_figure(f, 10, 20)
        f.canvas.manager.window.wm_geometry.assert_called_with("+10+20")

    @mock.patch('framework.utils.matplotlib')
    def test_move_wxagg(self, mock_mpl):
        mock_mpl.get_backend.return_value = 'WXAgg'
        f = mock.Mock()
        move_figure(f, 10, 20)
        f.canvas.manager.window.SetPosition.assert_called_with((10, 20))

    @mock.patch('framework.utils.matplotlib')
    def test_move_other(self, mock_mpl):
        mock_mpl.get_backend.return_value = 'anything_else'
        f = mock.Mock()
        move_figure(f, 10, 20)
        f.canvas.manager.window.move.assert_called_with(10, 20)


if __name__ == '__main__':
    unittest.main()
