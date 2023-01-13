import API.binary_manipulation as bm
import unittest
from parameterized import parameterized

class TestBinaryManipulation(unittest.TestCase):
    @parameterized.expand([[8, 0, 3, 0], [10, 0, 2, 2], [10, 2, 4, 2]])
    def test_get_sub_binary(self, bin, start, end, expected):
        out = bm.get_sub_binary(bin, start, end)
        self.assertEqual(expected, out)