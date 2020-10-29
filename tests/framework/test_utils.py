import unittest
from unittest import mock

import asyncio
import time

from framework.utils import worker


class WorkerTestCase(unittest.TestCase):

    def test_worker(self):

        class dummy():

            def __init__(self):
                self.updateinterval = 1

            def update(self, arg):
                time.sleep(1.0)

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


if __name__ == '__main__':
    unittest.main()
