from moviepy.editor import VideoFileClip
from flask import send_from_directory
import os
import file_manipulation as fm


def download_file(folder, name):
    return send_from_directory(folder, name)


def allowed_file(filename):
    return '.' in filename and fm.get_extension(filename) == 'mp4'


def convert(filename):
    clip = VideoFileClip(f'{filename}.mp4')
    clip.write_gif(f'{filename}.gif')
    clip.close()
    os.remove(f'{filename}.mp4')

