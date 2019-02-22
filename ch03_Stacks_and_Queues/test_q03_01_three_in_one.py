import unittest
from q03_01_three_in_one import three_in_one


class TestQ03_01ThreeInOne(unittest.TestCase):
    def setUp(self):
        self.arr_len = 20

    def test_three_in_one(self):
        a, b, c = three_in_one(self.arr_len)
        arr = []
        for e in a:
            arr.append(e)
        for e in b:
            arr.append(e)
        for e in c:
            arr.append(e)
        for i in range(self.arr_len):
            self.assertEqual(i, arr[i])


if __name__ == '__main__':
    unittest.main()
