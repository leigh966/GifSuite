from API.binary_manipulation import get_bit, get_sub_binary

class GifImage:
    def __init__(self, descriptor_bytes):
        self.__left = int.from_bytes(descriptor_bytes[2:0:-1],"big")
        self.__top = int.from_bytes(descriptor_bytes[4:2:-1],"big")
        self.__width = int.from_bytes(descriptor_bytes[6:4:-1],"big")
        self.__height = int.from_bytes(descriptor_bytes[8:6:-1],"big")
        self.__mip_byte = descriptor_bytes[9]

    __bits_per_pixel = None

    def get_bits_per_pixel(self):
        if self.__bits_per_pixel is None:
            self.__bits_per_pixel = get_sub_binary(self.__mip_byte, 0, 3)
        return self.__bits_per_pixel+1

    __is_interlaced = None

    def get_is_interlaced(self):
        if self.__is_interlaced is None:
            self.__is_interlaced = get_bit(self.__mip_byte, 6)
        return self.__is_interlaced

    __has_local_color_map = None

    def get_has_local_color_map(self):
        if self.__has_local_color_map is None:
            self.__has_local_color_map = get_bit(self.__mip_byte, 7)
        return self.__has_local_color_map

    def get_left(self):
        return self.__left

    def get_top(self):
        return self.__top

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height
