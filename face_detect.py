import cv2
import numpy


def get_faces_coordinates(image_data):
    # Create the haar cascade
    face_cascade = cv2.CascadeClassifier("../cascades/haarcascade_frontalface_default.xml")

    image = numpy.fromstring(image_data, dtype=numpy.uint8)
    image_np = cv2.imdecode(image, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return [{'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h)} for (x, y, w, h) in faces]
