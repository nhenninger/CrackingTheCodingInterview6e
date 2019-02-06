import unittest
from math import log10
from linked_list_node import LinkedListNode
from q02_05_sum_lists import (sum_lists_forward,
                              sum_lists_forward_recursive,
                              sum_lists_forward_stack,
                              sum_lists_reverse,
                              sum_lists_reverse_recursive)


class TestQ02_05SumLists(unittest.TestCase):
    def setUp(self):
        self.list_reverse_a = self.convert_to_reverse_linked_list(617)
        self.list_reverse_b = self.convert_to_reverse_linked_list(295)
        self.list_reverse_c = self.convert_to_reverse_linked_list(951)
        self.list_reverse_d = self.convert_to_reverse_linked_list(7632)
        self.list_reverse_e = self.convert_to_reverse_linked_list(879)
        self.list_reverse_f = self.convert_to_reverse_linked_list(586)

        self.list_forward_a = self.convert_to_forward_linked_list(617)
        self.list_forward_b = self.convert_to_forward_linked_list(295)
        self.list_forward_c = self.convert_to_forward_linked_list(951)
        self.list_forward_d = self.convert_to_forward_linked_list(7632)
        self.list_forward_e = self.convert_to_forward_linked_list(879)
        self.list_forward_f = self.convert_to_forward_linked_list(586)

        self.sum_ab = 617 + 295  # 912
        self.sum_cd = 951 + 7632  # 8583
        self.sum_ef = 879 + 586  # 1465

    def test_sum_lists_reverse(self):
        node_ab = sum_lists_reverse(self.list_reverse_a,
                                    self.list_reverse_b)
        node_cd = sum_lists_reverse(self.list_reverse_c,
                                    self.list_reverse_d)
        node_ef = sum_lists_reverse(self.list_reverse_e,
                                    self.list_reverse_f)
        self.check_reverse_list(node_ab, self.sum_ab)
        self.check_reverse_list(node_cd, self.sum_cd)
        self.check_reverse_list(node_ef, self.sum_ef)

    def test_sum_lists_reverse_recursive(self):
        node_ab = sum_lists_reverse_recursive(self.list_reverse_a,
                                              self.list_reverse_b)
        node_cd = sum_lists_reverse_recursive(self.list_reverse_c,
                                              self.list_reverse_d)
        node_ef = sum_lists_reverse_recursive(self.list_reverse_e,
                                              self.list_reverse_f)
        self.check_reverse_list(node_ab, self.sum_ab)
        self.check_reverse_list(node_cd, self.sum_cd)
        self.check_reverse_list(node_ef, self.sum_ef)

    def test_sum_lists_forward(self):
        node_ab = sum_lists_forward(self.list_forward_a,
                                    self.list_forward_b)
        node_cd = sum_lists_forward(self.list_forward_c,
                                    self.list_forward_d)
        node_ef = sum_lists_forward(self.list_forward_e,
                                    self.list_forward_f)
        self.check_forward_list(node_ab, self.sum_ab)
        self.check_forward_list(node_cd, self.sum_cd)
        self.check_forward_list(node_ef, self.sum_ef)

    def test_sum_lists_forward_recursive(self):
        node_ab = sum_lists_forward_recursive(self.list_forward_a,
                                              self.list_forward_b)
        node_cd = sum_lists_forward_recursive(self.list_forward_c,
                                              self.list_forward_d)
        node_ef = sum_lists_forward_recursive(self.list_forward_e,
                                              self.list_forward_f)
        self.check_forward_list(node_ab, self.sum_ab)
        self.check_forward_list(node_cd, self.sum_cd)
        self.check_forward_list(node_ef, self.sum_ef)

    def test_sum_lists_forward_stack(self):
        node_ab = sum_lists_forward_stack(self.list_forward_a,
                                          self.list_forward_b)
        node_cd = sum_lists_forward_stack(self.list_forward_c,
                                          self.list_forward_d)
        node_ef = sum_lists_forward_stack(self.list_forward_e,
                                          self.list_forward_f)
        self.check_forward_list(node_ab, self.sum_ab)
        self.check_forward_list(node_cd, self.sum_cd)
        self.check_forward_list(node_ef, self.sum_ef)

    @staticmethod
    def convert_to_reverse_linked_list(number: int) -> LinkedListNode:
        head = None
        while number > 0:
            digit = number % 10
            if head is None:
                head = LinkedListNode(digit)
            else:
                head.append_to_tail(digit)
            number //= 10
        return head

    @staticmethod
    def convert_to_forward_linked_list(number: int) -> LinkedListNode:
        # https://stackoverflow.com/questions/2189800/length-of-an-integer-in-python
        n = 1 if number == 0 else int(log10(number)) + 1
        head = None
        while n > 0:
            n -= 1
            digit = number // 10**n % 10
            if head is None:
                head = LinkedListNode(digit)
            else:
                head.append_to_tail(digit)
        return head

    def check_reverse_list(self, node: LinkedListNode, total: int) -> None:
        while node is not None:
            self.assertEqual(node.data, total % 10)
            total //= 10
            node = node.next

    def check_forward_list(self, node: LinkedListNode, total: int) -> None:
        n = 1 if total == 0 else int(log10(total)) + 1
        while node is not None:
            n -= 1
            self.assertEqual(node.data, total // 10**n % 10)
            node = node.next


if __name__ == '__main__':
    unittest.main()
