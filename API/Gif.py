from API.binary_manipulation import get_bit
class Gif:
    def __init__(self, gif_bytes):
        self.__version = gif_bytes[3:6]
        self.__width = int.from_bytes(gif_bytes[7:5:-1])
        self.__height = int.from_bytes(gif_bytes[9:7:-1])
        self.__has_global_color_map = get_bit(gif_bytes[13], 7)

    def get_has_global_color_map(self):
        return self.__has_global_color_map

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_version(self):
        return self.__version

    @staticmethod
    def read_from_file(path):
        with open(path, 'rb') as f:
            contents = f.read()
            return Gif(contents)


