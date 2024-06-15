import requests
from flask import *

app = Flask(__name__)


def get_image(id):
    return requests.get(f"http://stream-to-image/camera/{id}")


@app.route('/resize/<id>')
def resize_image(id):
    #test
    return get_image(id)


app.run("0.0.0.0", port=8081, debug=True)
