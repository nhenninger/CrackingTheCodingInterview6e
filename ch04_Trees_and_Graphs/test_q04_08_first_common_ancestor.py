import unittest
from nodes import BinaryTreeNode as BTNode
from q04_08_first_common_ancestor import first_common_ancestor


class TestQ04_08FirstCommonAncestor(unittest.TestCase):
    def setUp(self):
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

    def test_first_common_successor(self):
        self.assertEqual(first_common_ancestor(self.bt7, self.bt5_a, self.bt_root),
                         self.bt_root)
        self.assertEqual(first_common_ancestor(self.bt2, self.bt5_a, self.bt_root),
                         self.bt_root)
        self.assertEqual(first_common_ancestor(self.bt7, self.bt9, self.bt_root),
                         self.bt_root)
        self.assertEqual(first_common_ancestor(self.bt2, self.bt6, self.bt_root),
                         self.bt7)
        self.assertEqual(first_common_ancestor(self.bt2, self.bt5_b, self.bt_root),
                         self.bt7)
        self.assertEqual(first_common_ancestor(self.bt2, self.bt11, self.bt_root),
                         self.bt7)
        self.assertEqual(first_common_ancestor(self.bt4, self.bt11, self.bt_root),
                         self.bt_root)
        self.assertEqual(first_common_ancestor(self.bt2, self.bt7, self.bt_root),
                         self.bt7)
        self.assertEqual(first_common_ancestor(self.bt_root, self.bt9, self.bt_root),
                         self.bt_root)
        self.assertEqual(first_common_ancestor(self.bt5_b, self.bt11, self.bt_root),
                         self.bt6)
        self.assertEqual(first_common_ancestor(self.bt5_b, self.bt4, self.bt_root),
                         self.bt_root)


if __name__ == '__main__':
    unittest.main()
