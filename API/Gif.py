class Gif:
    def __init__(self, gif_bytes):
        self.version = gif_bytes[3:6]

    @staticmethod
    def read_from_file(path):
        with open(path, 'rb') as f:
            contents = f.read()
            return Gif(contents)
