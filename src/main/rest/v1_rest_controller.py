from flask import Flask, current_app, request
from main import IMAGES_DIRECTORY
import os
import json

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/images', methods=['GET'])
def get_images():
    return json.dumps(os.listdir(IMAGES_DIRECTORY))

@app.route('/images', methods=['POST'])
def post_image():
    with open(IMAGES_DIRECTORY + '/bo', 'wr') as f:
        f.write(request.form['image'])
    return ('', 204)
