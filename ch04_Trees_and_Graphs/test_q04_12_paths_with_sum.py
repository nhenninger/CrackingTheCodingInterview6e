import unittest
from nodes import BinaryTreeNode as BTNode
from q04_12_paths_with_sum import paths_with_sum


class TestQ04_12PathsWithSum(unittest.TestCase):
    def setUp(self) -> None:
        # https://en.wikipedia.org/wiki/File:Binary_tree.svg
        self.bt_root = BTNode(2)
        self.bt7 = BTNode(7)
        self.bt5_a = BTNode(5)
        self.bt_root.left = self.bt7
        self.bt_root.right = self.bt5_a
        self.bt2 = BTNode(2)
        self.bt6 = BTNode(6)
        self.bt7.left = self.bt2
        self.bt7.right = self.bt6
        self.bt9 = BTNode(9)
        self.bt5_a.right = self.bt9
        self.bt5_b = BTNode(5)
        self.bt11 = BTNode(11)
        self.bt6.left = self.bt5_b
        self.bt6.right = self.bt11
        self.bt4 = BTNode(4)
        self.bt9.left = self.bt4

    def test_paths_with_sum(self):
        self.assertEqual(1, paths_with_sum(self.bt_root, 16))
        self.assertEqual(1, paths_with_sum(self.bt_root, 24))
        self.assertEqual(1, paths_with_sum(self.bt_root, 26))
        self.assertEqual(2, paths_with_sum(self.bt_root, 2))
        self.assertEqual(2, paths_with_sum(self.bt_root, 13))
        self.assertEqual(2, paths_with_sum(self.bt_root, 20))
        self.assertEqual(3, paths_with_sum(self.bt_root, 9))
        self.assertEqual(3, paths_with_sum(self.bt_root, 11))


if __name__ == '__main__':
    unittest.main()
