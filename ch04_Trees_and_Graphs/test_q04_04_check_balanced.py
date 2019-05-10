import unittest
from nodes import BinaryTreeNode as BTNode
from q04_04_check_balanced import check_balanced


class TestQ04_04CheckBalanced(unittest.TestCase):
    def setUp(self):
        self.balanced_full_root = BTNode(0)
        self.bf1 = BTNode(1)
        self.bf2 = BTNode(2)
        self.balanced_full_root.left = self.bf1
        self.balanced_full_root.right = self.bf2
        self.bf3 = BTNode(3)
        self.bf4 = BTNode(4)
        self.bf1.left = self.bf3
        self.bf1.right = self.bf4
        self.bf5 = BTNode(5)
        self.bf6 = BTNode(6)
        self.bf2.left = self.bf5
        self.bf2.right = self.bf6

        self.balanced_not_full_root = BTNode(0)
        self.bnf1 = BTNode(1)
        self.bnf2 = BTNode(2)
        self.balanced_not_full_root.left = self.bnf1
        self.balanced_not_full_root.right = self.bnf2
        self.bnf3 = BTNode(3)
        self.bnf4 = BTNode(4)
        self.bnf1.left = self.bnf3
        self.bnf1.right = self.bnf4
        self.bnf5 = BTNode(5)
        self.bnf6 = BTNode(6)
        self.bnf2.left = self.bnf5
        self.bnf2.right = self.bnf6
        self.bnf7 = BTNode(7)
        self.bnf3.left = self.bnf7

        self.not_balanced_root = BTNode(0)
        self.nb1 = BTNode(1)
        self.nb2 = BTNode(2)
        self.not_balanced_root.left = self.nb1
        self.not_balanced_root.right = self.nb2
        self.nb3 = BTNode(3)
        self.nb1.left = self.nb3
        self.nb4 = BTNode(4)
        self.nb3.right = self.nb4
        self.nb5 = BTNode(5)
        self.nb4.left = self.nb5
        self.nb6 = BTNode(6)
        self.nb5.right = self.nb6

    def test_check_balanced(self):
        self.assertTrue(check_balanced(self.balanced_full_root))
        self.assertTrue(check_balanced(self.balanced_not_full_root))
        self.assertFalse(check_balanced(self.not_balanced_root))


if __name__ == '__main__':
    unittest.main()
