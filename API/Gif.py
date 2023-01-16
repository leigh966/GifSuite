from API.binary_manipulation import *
from API.ValueNotPresentError import ValueNotPresentError
from API.exception_generation import compare_values_equal, compare_values_in_range

NO_COLOR_MAP_MESSAGE = "This file does not contain a global color map"

class Gif:
    __global_color_map = None
    def __read_color_map(self, start):
        output = []
        for i in range(0, pow(2, self.__bits_per_pixel)):
            output.append([])
            byte_index = start+i*3
            for j in range(byte_index,byte_index+3):
                output[i].append(self.__gif_bytes[j])
        return output

    def __init__(self, gif_bytes):
        self.__gif_bytes = gif_bytes
        self.__version = gif_bytes[3:6]
        self.__width = int.from_bytes(gif_bytes[7:5:-1], "big")
        self.__height = int.from_bytes(gif_bytes[9:7:-1], "big")
        self.__has_global_color_map = get_bit(gif_bytes[10], 7)
        self.__color_resolution = flip_bin(get_sub_binary(gif_bytes[10], 4, 7))+1
        self.__bits_per_pixel = flip_bin(get_sub_binary(gif_bytes[10], 0, 3))+1
        self.__background_color_index = gif_bytes[11]

    def set_global_color_map(self, value):
        if not self.__has_global_color_map:
            return ValueNotPresentError(NO_COLOR_MAP_MESSAGE)
        compare_values_equal(pow(2, self.__bits_per_pixel), len(value), "The global color map should consist of 'expected' "
                                                                  "entries, not 'actual'")
        for entry_index in range(0, len(value)):
            compare_values_equal(3, len(value[entry_index]), "Each color should be made up of 'expected' values,"
                                                       " not 'actual'")
            for color_value in value[entry_index]:
                compare_values_in_range(0, 255, color_value, "Color values may only be between 0 and 255. Got 'actual'")
        self.__global_color_map = value


    def get_global_color_map(self):
        if not self.__has_global_color_map:
            raise ValueNotPresentError(NO_COLOR_MAP_MESSAGE)
        if self.__global_color_map is None:
            self.__global_color_map = self.__read_color_map(13)
        return self.__global_color_map

    def get_background_color_index(self):
        return self.__background_color_index

    def set_background_color_index(self, value):
        if value > pow(2, self.__bits_per_pixel) or value < 0:
            raise ValueError(f'Color index must be be an unsigned {self.__bits_per_pixel} bit integer')
        self.__background_color_index = value

    def get_bits_per_pixel(self):
        return self.__bits_per_pixel

    def get_color_resolution(self):
        return self.__color_resolution

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


