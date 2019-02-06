import unittest
from linked_list_node import LinkedListNode
from q02_04_partition import partition


class TestQ02_04Partition(unittest.TestCase):
    def setUp(self):
        self.head = LinkedListNode(3)
        elements = [5, 8, 5, 10, 2, 1]
        for e in elements:
            self.head.append_to_tail(e)

    def test_partition(self):
        partition_element = 5
        curr = partition(self.head, partition_element)
        count = 0
        while curr.data < partition_element:
            count += 1
            curr = curr.next
        while curr is not None:
            count += 1
            self.assertGreaterEqual(curr.data, partition_element)
            curr = curr.next
        self.assertEqual(count, 7)


if __name__ == '__main__':
    unittest.main()
