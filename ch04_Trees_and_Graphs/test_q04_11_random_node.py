import unittest
from q04_11_random_node import BinarySearchTreeNode as BSTNode


class TestQ04_11RandomNode(unittest.TestCase):
    def setUp(self) -> None:
        # https://en.wikipedia.org/wiki/File:Binary_search_tree.svg
        self.bst_root = BSTNode(8, None)
        self.bst_root.size = 9
        self.bst3 = BSTNode(3, self.bst_root)
        self.bst3.size = 5
        self.bst10 = BSTNode(10, self.bst_root)
        self.bst10.size = 3
        self.bst1 = BSTNode(1, self.bst3)
        self.bst1.size = 1
        self.bst6 = BSTNode(6, self.bst3)
        self.bst6.size = 3
        self.bst14 = BSTNode(14, self.bst10)
        self.bst14.size = 2
        self.bst4 = BSTNode(4, self.bst6)
        self.bst4.size = 1
        self.bst7 = BSTNode(7, self.bst6)
        self.bst4.size = 1
        self.bst13 = BSTNode(13, self.bst14)
        self.bst13.size = 1
        self.bst_root.left = self.bst3
        self.bst_root.right = self.bst10
        self.bst3.left = self.bst1
        self.bst3.right = self.bst6
        self.bst10.right = self.bst14
        self.bst6.left = self.bst4
        self.bst6.right = self.bst7
        self.bst14.left = self.bst13

    def test_insert(self):
        self.bst_root.insert(2)
        self.bst_root.insert(15)
        self.bst_root.insert(9)
        self.bst_root.insert(0)
        self.bst_root.insert(12)
        self.bst_root.insert(5)
        self.assertEqual(15, self.bst_root.size)
        self.assertEqual(3, self.bst1.size)
        self.assertEqual(8, self.bst3.size)
        self.assertEqual(4, self.bst14.size)
        self.assertEqual(2, self.bst1.right.data)
        self.assertEqual(15, self.bst14.right.data)
        self.assertEqual(9, self.bst10.left.data)
        self.assertEqual(0, self.bst1.left.data)
        self.assertEqual(12, self.bst13.left.data)
        self.assertEqual(5, self.bst4.right.data)

    def test_delete(self):
        self.bst_root.delete(14)
        self.assertTrue(self.bst10.right is self.bst13)
        self.bst_root.delete(1)
        self.assertTrue(self.bst3.left is None)
        self.assertTrue(self.bst3.right is self.bst6)

    def test_find(self):
        node = self.bst_root.find(13)
        self.assertTrue(node is self.bst13)
        node = self.bst_root.find(4)
        self.assertTrue(node is self.bst4)

    def test_get_random_node(self):
        NUM_SAMPLES = 5_000_000
        tallies = {}
        for i in range(NUM_SAMPLES):
            d = self.bst_root.get_random_node().data
            if d in tallies:
                tallies[d] += 1
            else:
                tallies[d] = 1
        self.assertEqual(9, len(tallies))
        fair_percent = 1 / len(tallies)
        for k in tallies.keys():
            actual_percent = tallies[k] / NUM_SAMPLES
            self.assertAlmostEqual(fair_percent, actual_percent, places=3)


if __name__ == '__main__':
    unittest.main()
