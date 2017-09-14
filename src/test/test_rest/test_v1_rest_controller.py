import mock
from main.rest import v1_rest_controller as module
from main import app
import os
import json
from StringIO import StringIO

client = app.test_client()

def test_get_images():
    module.IMAGES_DIRECTORY = 'test/contents'
    r = client.get('/images')
    assert r.get_data() ==json.dumps(os.listdir(module.IMAGES_DIRECTORY))

def test_post_image():
    module.IMAGES_DIRECTORY = 'test/contents'
    r = client.post('/images', data={'image': StringIO('fake image')})
    assert 'bo' in os.listdir(module.IMAGES_DIRECTORY)
    file_contents = ''
    with open(module.IMAGES_DIRECTORY + '/' + 'bo') as f:
        file_contents = f.read()
    assert file_contents == 'fake image'
    assert r.status_code == 204, '{} != {}'.format(r.status_code, 204)

    os.remove(module.IMAGES_DIRECTORY + '/' + 'bo')
