import unittest
from q01_05_one_away import one_away


class TestQ01_05OneAway(unittest.TestCase):
    def test_one_away(self):
        self.assertTrue(one_away('pale', 'ple'))
        self.assertTrue(one_away('pales', 'pale'))
        self.assertTrue(one_away('pale', 'bale'))
        self.assertTrue(one_away('apple', 'aple'))
        self.assertFalse(one_away('pale', 'bae'))


if __name__ == '__main__':
    unittest.main()
