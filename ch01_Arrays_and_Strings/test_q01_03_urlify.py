import unittest
from q01_03_urlify import urlify


class TestQ01_03TestUrlify(unittest.TestCase):
    def test_urlify(self):
        self.assertEqual(urlify(list('Mr John Smith    '), 13), list('Mr%20John%20Smith'))
        self.assertEqual(urlify(list('Mister Anderson  '), 15), list('Mister%20Anderson'))
        self.assertNotEqual(urlify(list('Mr  John Smith   '), 13), list('Mr%20John%20Smith'))


if __name__ == '__main__':
    unittest.main()
