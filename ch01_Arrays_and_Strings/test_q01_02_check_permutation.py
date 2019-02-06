import unittest
from q01_02_check_permutation import check_permutation


class TestQ01_02CheckPermutation(unittest.TestCase):
    def test_check_permutation(self):
        self.assertTrue(check_permutation('permutation', 'permutation'))
        self.assertTrue(check_permutation(' p e r m u t ation   ', 'p e r m u t a t i o n'))
        self.assertTrue(check_permutation('permutation', 'purmatiteon'))
        self.assertFalse(check_permutation('permutation', 'permanent'))
        self.assertFalse(check_permutation('permutation', 'p e r m u t a t i o n'))
        self.assertFalse(check_permutation('permutation', 'permutations'))
        self.assertFalse(check_permutation('permutations', 'permutation'))
        self.assertFalse(check_permutation('permutation1', 'permutation!'))
        self.assertFalse(check_permutation('p3rmu7a7ion', 'permutation'))


if __name__ == '__main__':
    unittest.main()
