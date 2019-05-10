import unittest
from nodes import BinaryTreeNode as BTNode, LinkedList, LinkedListNode as LLNode
from q04_03_list_of_depths import list_of_depths_dfs, list_of_depths_bfs


class TestQ04_03ListOfDepths(unittest.TestCase):
    def setUp(self):
        self.root = BTNode(0)
        self.n1 = BTNode(1)
        self.n2 = BTNode(2)
        self.root.left = self.n1
        self.root.right = self.n2
        self.n3 = BTNode(3)
        self.n4 = BTNode(4)
        self.n1.left = self.n3
        self.n1.right = self.n4
        self.n5 = BTNode(5)
        self.n6 = BTNode(6)
        self.n2.left = self.n5
        self.n2.right = self.n6

        self.lists = {0: LinkedList(),
                      1: LinkedList(),
                      2: LinkedList()}
        self.lists[0].add_node(LLNode(self.root))
        self.lists[1].add_node(LLNode(self.n1))
        self.lists[1].add_node(LLNode(self.n2))
        self.lists[2].add_node(LLNode(self.n3))
        self.lists[2].add_node(LLNode(self.n4))
        self.lists[2].add_node(LLNode(self.n5))
        self.lists[2].add_node(LLNode(self.n6))

    def test_list_of_depths_dfs(self):
        depths: dict = list_of_depths_dfs(self.root)
        for d in depths.keys():
            node = depths[d].head
            test = self.lists[d].head
            while node is not None:
                self.assertTrue(node.btn.data == test.btn.data)
                node = node.next
                test = test.next

    def test_list_of_depths_bfs(self):
        depths: dict = list_of_depths_bfs(self.root)
        for d in depths.keys():
            node = depths[d].head
            test = self.lists[d].head
            while node is not None:
                self.assertTrue(node.btn.data == test.btn.data)
                node = node.next
                test = test.next


if __name__ == '__main__':
    unittest.main()
