class Gif:
    def __init__(self, gif_bytes):
        self.version = gif_bytes[3:6]
        self.width = int.from_bytes(gif_bytes[7:5:-1])
        self.height = int.from_bytes(gif_bytes[9:7:-1])
        self.__has_global_color_map = gif_bytes[13] & 1 != 0

    def get_has_global_color_map(self):
        return self.__has_global_color_map

    @staticmethod
    def read_from_file(path):
        with open(path, 'rb') as f:
            contents = f.read()
            return Gif(contents)
