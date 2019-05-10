import unittest
from q04_06_successor import SuccessorNode, successor


class TestQ04_06Successor(unittest.TestCase):
    def setUp(self):
        # https://en.wikipedia.org/wiki/File:Binary_search_tree.svg
        self.bst_root = SuccessorNode(8)
        self.bst3 = SuccessorNode(3, self.bst_root)
        self.bst10 = SuccessorNode(10, self.bst_root)
        self.bst_root.left = self.bst3
        self.bst_root.right = self.bst10
        self.bst1 = SuccessorNode(1, self.bst3)
        self.bst6 = SuccessorNode(6, self.bst3)
        self.bst3.left = self.bst1
        self.bst3.right = self.bst6
        self.bst14 = SuccessorNode(14, self.bst10)
        self.bst10.right = self.bst14
        self.bst4 = SuccessorNode(4, self.bst6)
        self.bst7 = SuccessorNode(7, self.bst6)
        self.bst6.left = self.bst4
        self.bst6.right = self.bst7
        self.bst13 = SuccessorNode(13, self.bst14)
        self.bst14.left = self.bst13

    def test_successor(self):
        self.assertEqual(successor(self.bst1), self.bst3)
        self.assertEqual(successor(self.bst3), self.bst4)
        self.assertEqual(successor(self.bst4), self.bst6)
        self.assertEqual(successor(self.bst6), self.bst7)
        self.assertEqual(successor(self.bst7), self.bst_root)
        self.assertEqual(successor(self.bst_root), self.bst10)
        self.assertEqual(successor(self.bst10), self.bst13)
        self.assertEqual(successor(self.bst13), self.bst14)
        self.assertEqual(successor(self.bst14), None)
        self.assertNotEqual(successor(self.bst_root), self.bst_root)
        self.assertNotEqual(successor(self.bst_root), self.bst3)
        self.assertNotEqual(successor(self.bst_root), self.bst14)
        self.assertNotEqual(successor(self.bst6), self.bst_root)
        self.assertNotEqual(successor(self.bst6), self.bst13)
        self.assertNotEqual(successor(self.bst6), self.bst10)
        self.assertNotEqual(successor(self.bst14), self.bst13)


if __name__ == '__main__':
    unittest.main()
