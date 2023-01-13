from API.Gif import Gif
import unittest


class TestGif(unittest.TestCase):
    def test_version_correct(self):
        with open("data/tsTimer.gif", 'rb') as f:
            contents = f.read()
            my_gif = Gif(contents)
            b = bytes("89a", 'utf-8')
            self.assertEqual(b, my_gif.version)

    def test_read_from_file(self):
        manual = ()
        path = "data/tsTimer.gif"
        with open(path, 'rb') as f:
            contents = f.read()
            manual = Gif(contents)
        auto = Gif.read_from_file(path)
        self.assertEqual(auto.version, manual.version, "Using read_from_file should yield the " +
                                                       "same results as manually reading and passing in bytes")



if __name__ == '__main__':
    unittest.main()

