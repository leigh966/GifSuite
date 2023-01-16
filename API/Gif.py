from API.binary_manipulation import *
from API.ValueNotPresentError import ValueNotPresentError
from API.exception_generation import compare_values_equal, compare_values_in_range
from API.gif_processing import read_color_map

NO_COLOR_MAP_MESSAGE = "This file does not contain a global color map"
COLOR_START = 13
IMAGE_SEPERATOR = 44
EXTENSION_BLOCK_MARKER = 33


class Gif:
    __global_color_map = None

    def __init__(self, gif_bytes):
        self.__gif_bytes = gif_bytes
        self.__version = gif_bytes[3:6]
        self.__width = int.from_bytes(gif_bytes[7:5:-1], "big")
        self.__height = int.from_bytes(gif_bytes[9:7:-1], "big")
        self.__has_global_color_map = get_bit(gif_bytes[10], 7)
        self.__color_resolution = flip_bin(get_sub_binary(gif_bytes[10], 4, 7))+1
        self.__bits_per_pixel = flip_bin(get_sub_binary(gif_bytes[10], 0, 3))+1
        self.__background_color_index = gif_bytes[11]



    __image_descriptor_start = None

    def get_image_descriptor_start(self):
        def search_for_start_of_image_descriptor(current_index):
            if self.__gif_bytes[current_index] != EXTENSION_BLOCK_MARKER:
                return current_index
            current_index += 2
            while self.__gif_bytes[current_index] > 0:
                current_index += self.__gif_bytes[current_index] + 1
            return search_for_start_of_image_descriptor(current_index + 1)
        if self.__image_descriptor_start is None:
            base_start = (pow(2, self.__bits_per_pixel) * 3) + COLOR_START
            index = search_for_start_of_image_descriptor(base_start)
            if self.__gif_bytes[index] != IMAGE_SEPERATOR:
                raise ValueError(f'The read head got lost at index {index}'
                                 f' trying to find the start of the image descriptor')
            self.__image_descriptor_start = index
        return index

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
            self.__global_color_map = read_color_map(COLOR_START, self.__bits_per_pixel, self.__gif_bytes)
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


