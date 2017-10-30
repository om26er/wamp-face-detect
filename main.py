from autobahn.twisted.wamp import ApplicationSession
from twisted.internet.defer import inlineCallbacks

import face_detect


class MyComponent(ApplicationSession):
    @inlineCallbacks
    def onJoin(self, details):
        yield self.register(face_detect.get_faces_coordinates, "io.crossbar.detect_faces")
