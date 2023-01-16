from API.GifImage import GifImage
import unittest
from parameterized import parameterized


class TestGifImage(unittest.TestCase):
    @parameterized.expand([[b',\x00\x00\x00\x00\xaa\x01\xf0\x00', 0, 0, 426, 240]])
    def test_image_placement(self, input_bytes, expected_left, expected_top, expected_width, expected_height):
        gif_image = GifImage(bytes(input_bytes))
        names = ["left", "top", "width", "height"]
        expecteds = [expected_left, expected_top, expected_width, expected_height]
        actuals = [gif_image.get_left(), gif_image.get_top(), gif_image.get_width(), gif_image.get_height()]
        for i in range(0, len(names)):
            with self.subTest(name=names[i]):
                self.assertEqual(actuals[i], expecteds[i])


if __name__ == '__main__':
    unittest.main()