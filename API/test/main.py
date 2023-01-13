import os.path
import requests
import glob

API_URL = 'http://localhost:5000'
TEST_DATA_FOLDER = 'data'

def convert_file(filename):
    path = os.path.join(TEST_DATA_FOLDER, filename)
    print("opening "+path)
    with open(path, 'rb') as f:
        r = requests.post(API_URL+"/mp4ToGif", files={'file': f})
        assert(r.status_code == 200)
        print(f'TEST PASSED: Successfully converted "{filename}" to .gif')


os.chdir(TEST_DATA_FOLDER)
my_files = glob.glob('*.mp4')
os.chdir("..")
for file in my_files:
    convert_file(file)
