import unittest
from linked_list_node import LinkedListNode
from q02_01_remove_dups import remove_dups, remove_dups_no_buffer


class TestQ02_01RemoveDups(unittest.TestCase):
    def setUp(self):
        self.head = LinkedListNode(0)
        for i in range(20):
            self.head.append_to_tail(i % 5)

    def test_remove_dups(self):
        remove_dups(self.head)
        self.assertEqual(self.count_nodes(), 5)

    def test_remove_dups_no_buffer(self):
        remove_dups_no_buffer(self.head)
        self.assertEqual(self.count_nodes(), 5)

    def count_nodes(self) -> int:
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count


if __name__ == '__main__':
    unittest.main()
