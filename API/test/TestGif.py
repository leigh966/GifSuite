from API.Gif import Gif
import unittest
from parameterized import parameterized


class TestGif(unittest.TestCase):
    def test_version_correct(self):
        with open("data/tsTimer.gif", 'rb') as f:
            contents = f.read()
            my_gif = Gif(contents)
            b = bytes("89a", 'utf-8')
            self.assertEqual(b, my_gif.get_version())

    def test_read_from_file(self):
        manual = ()
        path = "data/tsTimer.gif"
        with open(path, 'rb') as f:
            contents = f.read()
            manual = Gif(contents)
        auto = Gif.read_from_file(path)
        self.assertEqual(auto.get_version(), manual.get_version(), "Using read_from_file should yield the " +
                                                       "same results as manually reading and passing in bytes")

    @parameterized.expand([["data/tsTimer.gif", True]])
    def test_has_color_map_correct(self, file_path, expected):
        self.assertEqual(expected, Gif.read_from_file(file_path).get_has_global_color_map())


    @parameterized.expand([["data/tsTimer.gif", 240], ["data/tsTimerCropped.gif", 180]])
    def test_height_correct(self, file_path, expected_height):
        gif = Gif.read_from_file(file_path)
        self.assertEqual(expected_height, gif.get_height())

    @parameterized.expand([["data/tsTimer.gif", 426], ["data/tsTimerCropped.gif", 319]])
    def test_width_correct(self, file_path, expected_width):
        gif = Gif.read_from_file(file_path)
        self.assertEqual(expected_width, gif.get_width())

    @parameterized.expand([["data/tsTimer.gif", 1]])
    def test_color_resolution_correct(self, file_path, expected):
        gif = Gif.read_from_file(file_path)
        self.assertEqual(expected, gif.get_color_resolution())

    @parameterized.expand([["data/tsTimer.gif", 8]])
    def test_bits_per_pixel_correct(self, file_path, expected):
        gif = Gif.read_from_file(file_path)
        self.assertEqual(expected, gif.get_bits_per_pixel())

    @parameterized.expand([["data/tsTimer.gif", 0]])
    def test_background_color_index_correct(self, file_path, expected):
        gif = Gif.read_from_file(file_path)
        self.assertEqual(expected, gif.get_background_color_index())

    @parameterized.expand([[-1, False], [0, True], [0b11111111, True], [0b11111111+1, False]])
    def test_set_background_color_index(self, value, allowed):
        gif = Gif.read_from_file("data/tsTimer.gif")
        start = gif.get_background_color_index()
        try:
            gif.set_background_color_index(value)
            self.assertEqual(value, gif.get_background_color_index())
        except ValueError:
            self.assertFalse(allowed)
            self.assertEqual(start, gif.get_background_color_index())


if __name__ == '__main__':
    unittest.main()

