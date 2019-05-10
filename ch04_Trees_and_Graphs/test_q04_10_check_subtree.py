import unittest
from nodes import BinaryTreeNode as BTNode
from q04_10_check_subtree import check_subtree


class TestQ04_10CheckSubtree(unittest.TestCase):
    def setUp(self) -> None:
        self.bt_root = BTNode(0)
        self.bt1 = BTNode(1)
        self.bt2 = BTNode(2)
        self.bt_root.left = self.bt1
        self.bt_root.right = self.bt2
        self.bt3 = BTNode(3)
        self.bt4 = BTNode(4)
        self.bt1.left = self.bt3
        self.bt1.right = self.bt4
        self.bt5 = BTNode(5)
        self.bt6 = BTNode(6)
        self.bt2.left = self.bt5
        self.bt2.right = self.bt6
        self.lonely_node = BTNode(42)

    def test_check_subtree(self):
        self.assertTrue(check_subtree(self.bt_root, self.bt1))
        self.assertTrue(check_subtree(self.bt_root, self.bt2))
        self.assertTrue(check_subtree(self.bt_root, self.bt3))
        self.assertTrue(check_subtree(self.bt_root, self.bt4))
        self.assertTrue(check_subtree(self.bt_root, self.bt5))
        self.assertTrue(check_subtree(self.bt_root, self.bt6))
        self.assertFalse(check_subtree(self.bt1, self.bt2))
        self.assertFalse(check_subtree(self.bt_root, self.lonely_node))


if __name__ == '__main__':
    unittest.main()
