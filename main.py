import os
from flask import Flask, flash, redirect, request
from werkzeug.utils import secure_filename
from moviepy.editor import VideoFileClip
from flask import send_from_directory

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['APPLICATION_ROOT'] = '/'

def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def do_conversion(filename):
    clip = VideoFileClip(f'{filename}.mp4')
    clip.write_gif(f'{filename}.gif')
    clip.close()
    os.remove(f'{filename}.mp4')

def remove_extension(filename):
    filename_parts = filename.split('.')
    output = ''
    for index in range(0,len(filename_parts)-1):
        output += filename_parts[index]
    return output

@app.route('/', methods=['POST'])
def convert():
    # check if the post request has the file part
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = remove_extension(secure_filename(file.filename))
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path+".mp4")
        do_conversion(path)
        return download_file(f'{filename}.gif')

app.run()
