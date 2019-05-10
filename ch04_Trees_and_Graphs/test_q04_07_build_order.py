import unittest
from q04_07_build_order import build_order, Project


class TestQ04_07BuildOrder(unittest.TestCase):
    def setUp(self):
        self.projects = ["a", "b", "c", "d", "e", "f", ]

        self.dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c"), ]

    def test_increment(self):
        order = build_order(self.projects, self.dependencies)
        self.assertTrue(order == "f e a b d c" or order == "e f a b d c")


if __name__ == '__main__':
    unittest.main()
