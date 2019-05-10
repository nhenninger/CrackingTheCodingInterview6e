import unittest
from nodes import BinaryTreeNode
from q04_02_minimal_tree import minimal_tree


class TestQ04_02MinimalTree(unittest.TestCase):
    def setUp(self):
        self.arr0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.arr1 = [0, 1, 2, 3, 4, 5, 6]

    def test_minimal_tree(self):
        self.assertTrue(self.is_bst(minimal_tree(self.arr0),
                                    self.arr0[0],
                                    self.arr0[len(self.arr0) - 1]))
        self.assertTrue(self.is_bst(minimal_tree(self.arr1),
                                    self.arr1[0],
                                    self.arr1[len(self.arr1) - 1]))

    def is_bst(self, root: BinaryTreeNode, lower: int, upper: int) -> bool:
        if root is None:
            return True
        if root.data < lower or root.data > upper:
            return False
        return (self.is_bst(root.left, lower, upper - 1) and
                self.is_bst(root.right, lower + 1, upper))


if __name__ == '__main__':
    unittest.main()
