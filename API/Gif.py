class Gif:
    def __init__(self, bytes):
        self.version = bytes[3:6]
