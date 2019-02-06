import unittest
from q01_06_string_compression import string_compression


class TestQ01_06StringCompression(unittest.TestCase):
    def test_string_compression(self):
        self.assertEqual(string_compression('aabcccccaaa'), 'a2b1c5a3')
        self.assertEqual(string_compression('aabbccdd'), 'aabbccdd')
        self.assertEqual(string_compression('abcd'), 'abcd')
        self.assertEqual(string_compression('aaa   bbb   ccc'), 'a3 3b3 3c3')
        self.assertEqual(string_compression('aaa^^^bbb^^^ccc'), 'a3^3b3^3c3')
        self.assertEqual(string_compression('a^b^c'), 'a^b^c')


if __name__ == '__main__':
    unittest.main()
