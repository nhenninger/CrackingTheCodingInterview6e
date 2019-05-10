import unittest
from nodes import BinaryTreeNode as BTNode
from q04_05_validate_bst import validate_bst, validate_bst_no_array, validate_bst_allow_dupes


class TestQ05_05ValidateBst(unittest.TestCase):
    def setUp(self):
        # https://en.wikipedia.org/wiki/File:Binary_search_tree.svg
        self.bst_root = BTNode(8)
        self.bst3 = BTNode(3)
        self.bst10 = BTNode(10)
        self.bst1 = BTNode(1)
        self.bst6 = BTNode(6)
        self.bst14 = BTNode(14)
        self.bst4 = BTNode(4)
        self.bst7 = BTNode(7)
        self.bst13 = BTNode(13)
        self.bst_root.left = self.bst3
        self.bst_root.right = self.bst10
        self.bst3.left = self.bst1
        self.bst3.right = self.bst6
        self.bst10.right = self.bst14
        self.bst6.left = self.bst4
        self.bst6.right = self.bst7
        self.bst14.left = self.bst13

        self.not_bst_root = BTNode(8)
        self.not_bst3 = BTNode(3)
        self.not_bst10 = BTNode(10)
        self.not_bst1 = BTNode(1)
        self.not_bst6 = BTNode(6)
        self.not_bst14 = BTNode(14)
        self.not_bst4 = BTNode(4)
        self.not_bst7 = BTNode(7)
        self.not_bst42 = BTNode(42)
        self.not_bst_root.left = self.not_bst3
        self.not_bst_root.right = self.not_bst10
        self.not_bst3.left = self.bst1
        self.not_bst3.right = self.not_bst6
        self.not_bst10.right = self.not_bst14
        self.not_bst6.left = self.not_bst4
        self.not_bst6.right = self.not_bst7
        self.not_bst14.left = self.not_bst42

    def test_validate_bst(self):
        self.assertTrue(validate_bst(self.bst_root))
        self.assertFalse(validate_bst(self.not_bst_root))

    def test_validate_bst_no_array(self):
        self.assertTrue(validate_bst_no_array(self.bst_root))
        self.assertFalse(validate_bst_no_array(self.not_bst_root))

    def test_validate_bst_allow_dupes(self):
        self.assertTrue(validate_bst_allow_dupes(self.bst_root))
        self.assertFalse(validate_bst_allow_dupes(self.not_bst_root))

    def test_validate_bst_allow_dupes_with_dupes(self):
        self.bst13_dupe = BTNode(13)
        self.bst13.left = self.bst13_dupe
        self.assertTrue(validate_bst_allow_dupes(self.bst_root))
        self.bst13.left = None
        self.bst13.right = self.bst13_dupe
        self.assertFalse(validate_bst_allow_dupes(self.bst_root))


if __name__ == '__main__':
    unittest.main()
