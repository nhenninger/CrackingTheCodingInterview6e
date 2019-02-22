import unittest
from q03_03_stack_of_plates import SetOfStacks


class TestQ03_03StackOfPlates(unittest.TestCase):
    def setUp(self):
        self.set_of_stacks = SetOfStacks()
        for i in range(42 ** 2):
            self.set_of_stacks.push(i)

    def test_pop(self):
        self.assertEqual(self.set_of_stacks.pop(), 42 ** 2 - 1)
        self.assertEqual(self.set_of_stacks.pop(), 42 ** 2 - 2)
        self.assertEqual(self.set_of_stacks.pop(), 42 ** 2 - 3)

    def test_pop_at(self):
        self.assertEqual(self.set_of_stacks.pop_at(0), 42 - 1)
        self.assertEqual(self.set_of_stacks.pop_at(1), 42 * 2 - 1)
        self.assertEqual(self.set_of_stacks.pop_at(2), 42 * 3 - 1)
        self.assertEqual(self.set_of_stacks.pop_at(16), 42 * 17 - 1)
        self.assertEqual(self.set_of_stacks.pop_at(41), 42 ** 2 - 1)
        self.assertEqual(self.set_of_stacks.pop_at(40), 42 ** 2 - 42 - 1)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            self.set_of_stacks.pop_at(1337)
        with self.assertRaises(ValueError):
            self.set_of_stacks.pop_at(-1)


if __name__ == '__main__':
    unittest.main()
