import asyncio
import argparse
import os
import sys

from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner


class MyComponent(ApplicationSession):
    async def onJoin(self, details):
        with open(photo, 'rb') as f:
            data = f.read()
        result = await self.call("io.crossbar.detect_faces", data)
        print(result)
        asyncio.get_event_loop().stop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    photo = os.path.abspath(os.path.expanduser(args.file))
    if not os.path.exists(photo):
        print('File "{}" does not exist'.format(photo))
        sys.exit(1)
    runner = ApplicationRunner("ws://127.0.0.1:8080/ws", u"realm1")
    runner.run(MyComponent)
