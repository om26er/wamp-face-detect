from os import environ
from urllib.parse import urlparse

import cv2
import numpy

from autobahn.asyncio.component import Component, run

URL = urlparse(environ.get("AUTOBAHN_DEMO_ROUTER", u"ws://127.0.0.1:8080/ws"))
component = Component(
    transports=[
        {
            "type": "websocket",
            "url": URL.geturl(),
            "endpoint": {
                "type": "tcp",
                "host": "localhost",
                "port": URL.port
            },
            "options": {
                "open_handshake_timeout": 100,
            }
        },
    ],
    realm=environ.get("AUTOBAHN_DEMO_REALM", u"realm1"),
)


@component.register("io.crossbar.demo.cvengine.detect_faces")
def get_faces_coordinates(image_data):
    # Create the haar cascade
    face_cascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

    image = numpy.fromstring(image_data, dtype=numpy.uint8)
    image_np = cv2.imdecode(image, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))
    return [{'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h)} for (x, y, w, h) in faces]


if __name__ == '__main__':
    run([component])
