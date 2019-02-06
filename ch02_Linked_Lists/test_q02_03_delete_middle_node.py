import unittest
from linked_list_node import LinkedListNode
from q02_03_delete_middle_node import delete_middle_node


class TestQ02_03DeleteMiddleNode(unittest.TestCase):
    def setUp(self):
        self.head_a = LinkedListNode(ord('a'))
        for i in range(5):
            self.head_a.append_to_tail(ord('b') + i)
        self.head_b = LinkedListNode(1)
        self.head_b.append_to_tail(5)
        self.head_b.append_to_tail(9)
        self.head_b.append_to_tail(12)

    def test_delete_middle_node(self):
        curr = self.head_a
        while curr.data != ord('c'):
            curr = curr.next
        delete_middle_node(curr)
        self.assertEqual(self.convert_linked_list_to_string(), 'abdef')

        curr = self.head_b
        while curr.data != 9:
            curr = curr.next
        delete_middle_node(curr)
        curr = self.head_b
        self.assertEqual(curr.data, 1)
        curr = curr.next
        self.assertEqual(curr.data, 5)
        curr = curr.next
        self.assertEqual(curr.data, 12)

    def convert_linked_list_to_string(self) -> str:
        curr = self.head_a
        letters = []
        while curr is not None:
            letters.append(chr(curr.data))
            curr = curr.next
        return ''.join(letters)


if __name__ == '__main__':
    unittest.main()
