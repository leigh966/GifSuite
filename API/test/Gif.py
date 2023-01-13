from API.Gif import Gif

def test_version():
    with open("data/tsTimer.gif", 'rb') as f:
        contents = f.read()
        my_gif = Gif(contents)
        b = bytes("89a", 'utf-8')
        assert(my_gif.version == b)

test_version()

