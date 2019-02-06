import unittest
from q01_07_rotate_matrix import rotate_matrix, rotate_matrix_inplace


class TestQ01_07RotateMatrix(unittest.TestCase):
    def setUp(self):
        self.original_matrix_a = [[1, 2],
                                  [3, 4], ]

        self.original_matrix_b = [[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 8, 9]]

        self.original_matrix_c = [[1, 2, 3, 4],
                                  [5, 6, 7, 8],
                                  [9, 10, 11, 12],
                                  [13, 14, 15, 16], ]

        self.rotated_matrix_a = [[2, 4],
                                 [1, 3], ]

        self.rotated_matrix_b = [[3, 6, 9],
                                 [2, 5, 8],
                                 [1, 4, 7], ]

        self.rotated_matrix_c = [[4, 8, 12, 16],
                                 [3, 7, 11, 15],
                                 [2, 6, 10, 14],
                                 [1, 5, 9, 13], ]

    def test_rotate_matrix(self):
        self.assertEqual(rotate_matrix(
            self.original_matrix_a, 2), self.rotated_matrix_a)
        self.assertEqual(rotate_matrix(
            self.original_matrix_b, 3), self.rotated_matrix_b)
        self.assertEqual(rotate_matrix(
            self.original_matrix_c, 4), self.rotated_matrix_c)

    def test_rotate_matrix_inplace(self):
        self.assertEqual(rotate_matrix_inplace(
            self.original_matrix_a, 2), self.rotated_matrix_a)
        self.assertEqual(rotate_matrix_inplace(
            self.original_matrix_b, 3), self.rotated_matrix_b)
        self.assertEqual(rotate_matrix_inplace(
            self.original_matrix_c, 4), self.rotated_matrix_c)


if __name__ == '__main__':
    unittest.main()
