import unittest
from q03_02_stack_min import StackMin, StackMinNode


class TestQ03_02StackMin(unittest.TestCase):
    def setUp(self):
        self.stack_min = StackMin()
        self.stack_min.push(0)
        self.stack_min.push(10)
        self.stack_min.push(1)
        self.stack_min.push(9)
        self.stack_min.push(8)
        self.stack_min.push(7)
        self.stack_min.push(5)
        self.stack_min.push(16)
        self.stack_min.push(-1)
        self.stack_min.push(42)
        self.stack_min.push(-69)

    def test_stack_minimum(self):
        self.assertEqual(self.stack_min.minimum(), -69)

    def test_stack_minimum_after_pop(self):
        self.stack_min.pop()
        self.assertEqual(self.stack_min.minimum(), -1)
        self.stack_min.pop()
        self.stack_min.pop()
        self.assertEqual(self.stack_min.minimum(), 0)


if __name__ == '__main__':
    unittest.main()
