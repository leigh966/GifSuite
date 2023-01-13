from API.Gif import Gif
import unittest


class TestGif(unittest.TestCase):
    def test_version_correct(self):
        with open("data/tsTimer.gif", 'rb') as f:
            contents = f.read()
            my_gif = Gif(contents)
            b = bytes("89a", 'utf-8')
            self.assertEqual(b, my_gif.version)


if __name__ == '__main__':
    unittest.main()

