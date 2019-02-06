import unittest
from random import shuffle
from q03_05_sort_stack import sort_stack


class Test_Q03_05_Sort_Stack(unittest.TestCase):
    def setUp(self):
        self.stack_A = [i for i in range(20)]
        self.stack_B = [i * i for i in range(20)]
        self.stack_C = [i for i in range(20, -1, -1)]
        self.stack_D = [i for i in range(20, -1, -1)]
        shuffle(self.stack_D)
        self.stack_E = [10, 0, 9, 1, 8, 2, 7, 3, 6, 4, 5]

    def test_sort_stack(self):
        a = sort_stack(self.stack_A)
        b = sort_stack(self.stack_B)
        c = sort_stack(self.stack_C)
        d = sort_stack(self.stack_D)
        e = sort_stack(self.stack_E)
        self.check_stack_sorted(a)
        self.check_stack_sorted(b)
        self.check_stack_sorted(c)
        self.check_stack_sorted(d)
        self.check_stack_sorted(e)

    def check_stack_sorted(self, stack: list) -> None:
        if stack is None:
            raise TypeError("Stack cannot be None")
        elif len(stack) == 0:
            raise ValueError("Stack cannot be empty")
        prev = stack[0]
        for i in range(1, len(stack)):
            self.assertGreater(prev, stack[i])
            prev = stack[i]


if __name__ == '__main__':
    unittest.main()
