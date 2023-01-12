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


@app.route('/', methods=['POST'])
def convert():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        directory = f'{UPLOAD_FOLDER}/{filename}'.split(".")[0]
        do_conversion(directory)
        return download_file(f'{filename.split(".")[0]}.gif')

app.run()
