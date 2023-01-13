import file_manipulation as fm


def allowed_file(filename):
    return '.' in filename and fm.get_extension(filename) == 'gif'