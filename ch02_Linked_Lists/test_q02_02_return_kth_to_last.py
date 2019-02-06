import unittest
from linked_list_node import LinkedListNode
from q02_02_return_kth_to_last import (return_kth_to_last,
                                       return_kth_to_last_recursive)


class TestQ02_02ReturnKthToLast(unittest.TestCase):
    def setUp(self):
        self.head = LinkedListNode(20)
        for i in range(19, -1, -1):
            self.head.append_to_tail(i)

    def test_return_kth_to_last(self):
        self.assertEqual(return_kth_to_last(self.head, 5), 5)
        self.assertEqual(return_kth_to_last(self.head, 15), 15)

    def test_return_kth_to_last_recursive(self):
        self.assertEqual(return_kth_to_last_recursive(self.head, 5), 5)
        self.assertEqual(return_kth_to_last_recursive(self.head, 15), 15)


if __name__ == '__main__':
    unittest.main()
