import asyncio
import argparse
import os
import sys

from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
import cv2
import numpy


class MyComponent(ApplicationSession):
    async def onJoin(self, details):
        with open(photo, 'rb') as f:
            data = f.read()
        faces = await self.call("io.crossbar.detect_faces", data)
        image_raw = numpy.fromstring(data, dtype=numpy.uint8)
        image_np = cv2.imdecode(image_raw, cv2.IMREAD_COLOR)
        for f in faces:
            cv2.rectangle(image_np, (f['x'], f['y']), (f['x'] + f['w'], f['y'] + f['h']),
                          (0, 255, 0), 2)
        cv2.imwrite('output.jpg', image_np)
        self.leave()

    def onDisconnect(self):
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
