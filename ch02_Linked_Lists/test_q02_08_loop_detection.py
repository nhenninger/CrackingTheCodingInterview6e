import unittest
from linked_list_node import LinkedListNode
from q02_08_loop_detection import loop_detection, loop_detection_no_buffer


class TestQ02_08LoopDetection(unittest.TestCase):
    def setUp(self):
        self.node_a = LinkedListNode(ord('a'))
        self.node_b = LinkedListNode(ord('b'))
        self.node_c = LinkedListNode(ord('c'))
        self.node_d = LinkedListNode(ord('d'))
        self.node_e = LinkedListNode(ord('e'))
        self.node_f = LinkedListNode(ord('f'))
        self.node_g = LinkedListNode(ord('g'))
        self.node_h = LinkedListNode(ord('h'))
        self.node_i = LinkedListNode(ord('i'))
        self.node_a.next = self.node_b
        self.node_b.next = self.node_c
        self.node_c.next = self.node_d
        self.node_d.next = self.node_e
        self.node_e.next = self.node_f
        self.node_f.next = self.node_g
        self.node_g.next = self.node_h
        self.node_h.next = self.node_i
        self.node_i.next = self.node_d

    def test_loop_detection(self):
        self.assertEqual(loop_detection(self.node_a), self.node_d)

    def test_loop_detection_no_buffer(self):
        self.assertEqual(loop_detection_no_buffer(self.node_a), self.node_d)


if __name__ == '__main__':
    unittest.main()
