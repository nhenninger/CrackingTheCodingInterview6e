import unittest
from q01_08_zero_matrix import zero_matrix, zero_matrix_constant_memory


class TestQ01_08ZeroMatrix(unittest.TestCase):
    def setUp(self):
        self.original_matrix_a = [[0, 2],
                                  [3, 4], ]

        self.original_matrix_b = [[1, 2, 3],
                                  [4, 0, 6],
                                  [7, 8, 9]]

        self.original_matrix_c = [[1, 2, 3, 4],
                                  [5, 0, 7, 8],
                                  [9, 10, 0, 12],
                                  [13, 14, 15, 16], ]

        self.zero_matrix_a = [[0, 0],
                              [0, 4], ]

        self.zero_matrix_b = [[1, 0, 3],
                              [0, 0, 0],
                              [7, 0, 9]]

        self.zero_matrix_c = [[1, 0, 0, 4],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [13, 0, 0, 16], ]

    def test_zero_matrix(self):
        self.assertEqual(zero_matrix(
            self.original_matrix_a, 2, 2), self.zero_matrix_a)
        self.assertEqual(zero_matrix(
            self.original_matrix_b, 3, 3), self.zero_matrix_b)
        self.assertEqual(zero_matrix(
            self.original_matrix_c, 4, 4), self.zero_matrix_c)

    def test_zero_matrix_constant_memory(self):
        self.assertEqual(zero_matrix_constant_memory(
            self.original_matrix_a, 2, 2), self.zero_matrix_a)
        self.assertEqual(zero_matrix_constant_memory(
            self.original_matrix_b, 3, 3), self.zero_matrix_b)
        self.assertEqual(zero_matrix_constant_memory(
            self.original_matrix_c, 4, 4), self.zero_matrix_c)


if __name__ == '__main__':
    unittest.main()
