import unittest
from nodes import BinaryTreeNode as BTNode
from q04_09_bst_sequences import bst_sequences


class TestQ04_09BstSequences(unittest.TestCase):
    def setUp(self) -> None:
        self.bst_root = BTNode(2)
        self.bst_root.left = BTNode(1)
        self.bst_root.right = BTNode(3)
        self.arr_A = [2, 1, 3]
        self.arr_B = [2, 3, 1]
        self.output_AB = str([self.arr_A, self.arr_B])
        self.output_BA = str([self.arr_B, self.arr_A])

    def test_bst_sequences(self):
        output = str(bst_sequences(self.bst_root))
        self.assertTrue(output == self.output_AB or output == self.output_BA)


if __name__ == '__main__':
    unittest.main()
