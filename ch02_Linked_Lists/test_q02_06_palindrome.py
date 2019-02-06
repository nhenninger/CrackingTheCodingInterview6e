import unittest
from linked_list_node import LinkedListNode
from q02_06_palindrome import (palindrome,
                               palindrome_recursive,
                               palindrome_reverse_list)


class TestQ02_06Palindrome(unittest.TestCase):
    def setUp(self):
        self.palindrome_a = self.convert_str_to_linked_list('Racecar')
        self.len_palindrome_a = 7
        self.palindrome_b = self.convert_str_to_linked_list('Taco cat')
        self.len_palindrome_b = 8
        self.palindrome_c = self.convert_str_to_linked_list('A butt tuba.')
        self.len_palindrome_c = 11
        self.palindrome_d = self.convert_str_to_linked_list('Able was I ere I saw Elba.')
        self.len_palindrome_d = 26

        self.not_palindrome_a = self.convert_str_to_linked_list('Banana')
        self.len_not_palindrome_a = 6
        self.not_palindrome_b = self.convert_str_to_linked_list('Palindrome')
        self.len_not_palindrome_b = 10

    def test_palindrome(self):
        self.assertTrue(palindrome(self.palindrome_a))
        self.assertTrue(palindrome(self.palindrome_b))
        self.assertFalse(palindrome(self.not_palindrome_a))
        self.assertFalse(palindrome(self.not_palindrome_b))

    def test_palindrome_recursive(self):
        self.assertTrue(palindrome_recursive(self.palindrome_a,
                                             self.len_palindrome_a))
        self.assertFalse(palindrome_recursive(self.not_palindrome_a,
                                              self.len_not_palindrome_a))
        self.assertFalse(palindrome_recursive(self.not_palindrome_b,
                                              self.len_not_palindrome_b))

    def test_palindrome_reverse_list(self):
        self.assertTrue(palindrome_reverse_list(self.palindrome_a))
        self.assertTrue(palindrome_reverse_list(self.palindrome_b))
        self.assertFalse(palindrome_reverse_list(self.not_palindrome_a))
        self.assertFalse(palindrome_reverse_list(self.not_palindrome_b))

    @staticmethod
    def convert_str_to_linked_list(s: str) -> LinkedListNode:
        if s is None or len(s) == 0:
            return None
        head = curr = None
        for i in range(len(s)):
            ch = ord(s[i])
            if head is None:
                head = LinkedListNode(ch)
                curr = head
            else:
                curr.next = LinkedListNode(ch)
                curr = curr.next
        return head


if __name__ == '__main__':
    unittest.main()
