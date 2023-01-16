class GifImage:
    def __init__(self, descriptor_bytes):
        self.__left = int.from_bytes(descriptor_bytes[2:0:-1],"big")
        self.__top = int.from_bytes(descriptor_bytes[4:2:-1],"big")
        self.__width = int.from_bytes(descriptor_bytes[6:4:-1],"big")
        self.__height = int.from_bytes(descriptor_bytes[8:6:-1],"big")

    def get_left(self):
        return self.__left

    def get_top(self):
        return self.__top

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height
