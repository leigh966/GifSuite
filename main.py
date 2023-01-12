import os
from flask import Flask, flash, redirect, request
from werkzeug.utils import secure_filename
import mp4_to_gif as m2g
import file_manipulation as fm


UPLOAD_FOLDER = 'uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['APPLICATION_ROOT'] = '/'

@app.route('/mp4ToGif', methods=['POST'])
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
    if file and m2g.allowed_file(file.filename):
        filename = fm.remove_extension(secure_filename(file.filename))
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path+".mp4")
        m2g.convert(path)
        return m2g.download_file(UPLOAD_FOLDER, f'{filename}.gif')

app.run()
