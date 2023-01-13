class Gif:
    def __init__(self, gif_bytes):
        self.version = gif_bytes[3:6]
