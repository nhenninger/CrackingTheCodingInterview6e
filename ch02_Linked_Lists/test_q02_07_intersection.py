import unittest
from linked_list_node import LinkedListNode
from q02_07_intersection import intersection, intersection_no_buffer


class TestQ02_07Intersection(unittest.TestCase):
    def setUp(self):
        self.node_a = LinkedListNode(ord('a'))
        self.node_c = LinkedListNode(ord('c'))
        self.node_f = LinkedListNode(ord('f'))
        self.node_t = LinkedListNode(ord('t'))
        self.node_c.next = self.node_a
        self.node_f.next = self.node_a
        self.node_a.next = self.node_t

    def test_intersection(self):
        self.assertEqual(intersection(self.node_c, self.node_f),
                         self.node_a)

    def test_intersection_no_buffer(self):
        self.assertEqual(intersection_no_buffer(self.node_c, self.node_f),
                         self.node_a)


if __name__ == '__main__':
    unittest.main()
