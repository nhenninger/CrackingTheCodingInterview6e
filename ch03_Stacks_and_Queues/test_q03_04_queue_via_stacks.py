import unittest
from q03_04_queue_via_stacks import MyQueue


class Test_Q03_04_Queue_Via_Stacks(unittest.TestCase):
    def setUp(self):
        self.my_queue = MyQueue()
        self.num_elements = 1337
        for i in range(self.num_elements):
            self.my_queue.push(i)

    def test_pop(self):
        for i in range(self.num_elements):
            self.assertEqual(i, self.my_queue.pop())


if __name__ == '__main__':
    unittest.main()
