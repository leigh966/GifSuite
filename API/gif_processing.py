import API.file_manipulation as fm


def allowed_file(filename):
    return '.' in filename and fm.get_extension(filename) == 'gif'


def read_color_map(start, bits_per_pixel, gif_bytes):
    output = []
    for i in range(0, pow(2, bits_per_pixel)):
        output.append([])
        byte_index = start+i*3
        for j in range(byte_index,byte_index+3):
            output[i].append(gif_bytes[j])
    return output