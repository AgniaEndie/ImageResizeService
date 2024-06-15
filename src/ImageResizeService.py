import requests
from flask import *
import cv2

app = Flask(__name__)


def get_image(id):
    localCamera = cv2.VideoCapture(f"http://stream-to-image-service/camera/{id}")
    success, frame = localCamera.read()
    return Response(frame, mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/resize/<id>')
def resize_image(id):
    # test
    return get_image(id)


app.run("0.0.0.0", port=8081, debug=True)
