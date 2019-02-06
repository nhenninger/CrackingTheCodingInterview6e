import unittest
from q01_01_is_unique import (is_unique,
                              is_unique_bit_vector,
                              is_unique_no_data_structures,
                              is_unique_sorted)


class TestQ01_01IsUnique(unittest.TestCase):
    def setUp(self):
        self.unique_string = "abcdef"
        self.duplicate_string = "abcdefabcdef"

    def test_is_unique(self):
        self.assertTrue(is_unique(self.unique_string))
        self.assertFalse(is_unique(self.duplicate_string))

    def test_is_unique_bit_vector(self):
        self.assertTrue(is_unique_bit_vector(self.unique_string))
        self.assertFalse(is_unique_bit_vector(self.duplicate_string))

    def test_is_unique_no_data_structures(self):
        self.assertTrue(is_unique_no_data_structures(self.unique_string))
        self.assertFalse(is_unique_no_data_structures(self.duplicate_string))

    def test_is_unique_sorted(self):
        self.assertTrue(is_unique_sorted(self.unique_string))
        self.assertFalse(is_unique_sorted(self.duplicate_string))


if __name__ == '__main__':
    unittest.main()
