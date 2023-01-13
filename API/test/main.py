import os.path
import requests
import glob
import unittest

API_URL = 'http://localhost:5000'
TEST_DATA_FOLDER = 'data'
def convert_file(filename):
    path = os.path.join(TEST_DATA_FOLDER, filename)
    with open(path, 'rb') as f:
        r = requests.post(API_URL + "/mp4ToGif", files={'file': f})
        assert (r.status_code == 200)


class TestMain(unittest.TestCase):
    def test_mp4ToGif_endpoint(self):
        os.chdir(TEST_DATA_FOLDER)
        my_files = glob.glob('*.mp4')
        os.chdir("..")
        for file in my_files:
            with self.subTest(filename=file):
                convert_file(file)
