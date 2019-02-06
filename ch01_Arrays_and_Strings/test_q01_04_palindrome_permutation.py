import unittest
from q01_04_palindrome_permutation import (palindrome_permutation,
                                           palindrome_permutation_bit_vector)


class TestQ01_04PalindromePermutation(unittest.TestCase):
    def test_palindrome_permutation(self):
        self.assertTrue(palindrome_permutation('Tact Coa'))
        self.assertTrue(palindrome_permutation('Nana'))
        self.assertTrue(palindrome_permutation('aabbcc'))
        self.assertTrue(palindrome_permutation('abbcc'))
        self.assertTrue(palindrome_permutation('a bb cc'))
        self.assertFalse(palindrome_permutation('Python'))

    def test_palindrome_permutation_bit_vector(self):
        self.assertTrue(palindrome_permutation_bit_vector('Tact Coa'))
        self.assertTrue(palindrome_permutation_bit_vector('Nana'))
        self.assertTrue(palindrome_permutation_bit_vector('aabbcc'))
        self.assertTrue(palindrome_permutation_bit_vector('abbcc'))
        self.assertTrue(palindrome_permutation_bit_vector('a bb cc'))
        self.assertFalse(palindrome_permutation_bit_vector('Python'))


if __name__ == '__main__':
    unittest.main()
