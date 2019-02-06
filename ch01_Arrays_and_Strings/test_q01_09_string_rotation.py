import unittest
from q01_09_string_rotation import string_rotation


class TestQ01_09StringRotation(unittest.TestCase):
    def test_string_rotation(self):
        self.assertTrue(string_rotation("erbottlewat","waterbottle"))
        self.assertTrue(string_rotation("waterbottle", "erbottlewat"))
        self.assertTrue(string_rotation("er bottlewat","water bottle"))
        self.assertFalse(string_rotation(" erbottlewat","waterbottle "))
        self.assertFalse(string_rotation("wat", "water"))


if __name__ == '__main__':
    unittest.main()
