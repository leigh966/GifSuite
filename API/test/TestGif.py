from API.Gif import Gif
import unittest
from parameterized import parameterized

MAIN_TEST_GIF = "data/tsTimer.gif"
CROPPED_TEST_GIF = "data/tsTimerCropped.gif"

class TestGif(unittest.TestCase):
    def test_version_correct(self):
        with open(MAIN_TEST_GIF, 'rb') as f:
            contents = f.read()
            my_gif = Gif(contents)
            b = bytes("89a", 'utf-8')
            self.assertEqual(b, my_gif.get_version())

    def test_read_from_file(self):
        manual = ()
        path = MAIN_TEST_GIF
        with open(path, 'rb') as f:
            contents = f.read()
            manual = Gif(contents)
        auto = Gif.read_from_file(path)
        self.assertEqual(auto.get_version(), manual.get_version(), "Using read_from_file should yield the " +
                                                                "same results as manually reading and passing in bytes")

    @parameterized.expand([[MAIN_TEST_GIF, True]])
    def test_has_color_map_correct(self, file_path, expected):
        self.assertEqual(expected, Gif.read_from_file(file_path).get_has_global_color_map())

    @parameterized.expand([[MAIN_TEST_GIF, 240], [CROPPED_TEST_GIF, 180]])
    def test_height_correct(self, file_path, expected_height):
        gif = Gif.read_from_file(file_path)
        self.assertEqual(expected_height, gif.get_height())

    @parameterized.expand([[MAIN_TEST_GIF, 426], [CROPPED_TEST_GIF, 319]])
    def test_width_correct(self, file_path, expected_width):
        gif = Gif.read_from_file(file_path)
        self.assertEqual(expected_width, gif.get_width())

    @parameterized.expand([[MAIN_TEST_GIF, 1]])
    def test_color_resolution_correct(self, file_path, expected):
        gif = Gif.read_from_file(file_path)
        self.assertEqual(expected, gif.get_color_resolution())

    @parameterized.expand([[MAIN_TEST_GIF, 8]])
    def test_bits_per_pixel_correct(self, file_path, expected):
        gif = Gif.read_from_file(file_path)
        self.assertEqual(expected, gif.get_bits_per_pixel())

    @parameterized.expand([[MAIN_TEST_GIF, 0]])
    def test_background_color_index_correct(self, file_path, expected):
        gif = Gif.read_from_file(file_path)
        self.assertEqual(expected, gif.get_background_color_index())

    @parameterized.expand([[MAIN_TEST_GIF, -1, False], [MAIN_TEST_GIF, 0, True], [MAIN_TEST_GIF, 0b11111111, True],
                           [MAIN_TEST_GIF, 0b11111111+1, False]])
    def test_set_background_color_index(self, file_path, value, allowed):
        gif = Gif.read_from_file(file_path)
        start = gif.get_background_color_index()
        try:
            gif.set_background_color_index(value)
            self.assertEqual(value, gif.get_background_color_index())
        except ValueError:
            self.assertFalse(allowed)
            self.assertEqual(start, gif.get_background_color_index())

    @parameterized.expand([[MAIN_TEST_GIF, 0, 246, 246, 246]])
    def test_global_color_map_correct(self, file_path, entry_no, red, green, blue):
        gif = Gif.read_from_file(file_path)
        color_entry = gif.get_global_color_map()[entry_no]
        self.assertEqual(red, color_entry[0])
        self.assertEqual(green, color_entry[1])
        self.assertEqual(blue, color_entry[2])

    @parameterized.expand([[MAIN_TEST_GIF, pow(2 ,8), [256, 255,255], False],
                           [MAIN_TEST_GIF, pow(2, 8), [255, 256,255], False],
                           [MAIN_TEST_GIF, pow(2, 8), [255, 255,256], False],
                           [MAIN_TEST_GIF, pow(2, 8), [255, 255,255], True],
                           [MAIN_TEST_GIF, pow(2, 8) - 1, [255, 255, 255], False],
                           [MAIN_TEST_GIF, pow(2, 8) + 1, [255, 255, 255], False],
                           [MAIN_TEST_GIF, pow(2, 8), [-1, 0, 0], False],
                           [MAIN_TEST_GIF, pow(2, 8), [0, -1, 0], False],
                           [MAIN_TEST_GIF, pow(2, 8), [0, 0, -1], False],
                           [MAIN_TEST_GIF, pow(2, 8), [0, 0, 0], True],
                           [MAIN_TEST_GIF, pow(2, 8), [0, 0, 0, 0], False],
                           [MAIN_TEST_GIF, pow(2, 8), [0, 0], False]])
    def test_set_global_color_map(self, file_path, no_entries, colors, allowed):
        color_map = []
        for i in range(0, no_entries):
            color_map.append(colors)
        gif = Gif.read_from_file(file_path)
        start = gif.get_global_color_map()
        try:
            gif.set_global_color_map(color_map)
            self.assertTrue(allowed)
            self.assertEqual(color_map, gif.get_global_color_map())
        except ValueError:
            self.assertFalse(allowed)
            self.assertEqual(start, gif.get_global_color_map())

    @parameterized.expand([[MAIN_TEST_GIF, 808]])
    def test_image_descriptor_start_correct(self, file_path, expected_start):
        gif = Gif.read_from_file(file_path)
        self.assertEqual(expected_start, gif.get_image_descriptor_start())


if __name__ == '__main__':
    unittest.main()

