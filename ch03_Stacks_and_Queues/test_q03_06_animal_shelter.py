import unittest
from q03_06_animal_shelter import (Animal,
                                   AnimalShelter,
                                   AnimalShelterTwoLists,
                                   Cat,
                                   Dog)


class TestQ03_06AnimalShelter(unittest.TestCase):
    def setUp(self):
        self.shelter_one = AnimalShelter()
        self.shelter_two = AnimalShelterTwoLists()

    def test_order(self):
        self.shelter_one.enqueue(Cat(0))
        self.shelter_one.enqueue(Cat(1))
        self.shelter_one.enqueue(Dog(2))
        self.shelter_one.enqueue(Dog(3))
        self.shelter_one.enqueue(Cat(4))
        self.shelter_one.enqueue(Cat(5))
        self.assertIsInstance(self.shelter_one.dequeue_any(), Cat)
        self.assertIsInstance(self.shelter_one.dequeue_dog(), Dog)
        self.assertIsInstance(self.shelter_one.dequeue_any(), Cat)
        self.assertIsInstance(self.shelter_one.dequeue_any(), Dog)
        self.shelter_two.enqueue(Cat(0))
        self.shelter_two.enqueue(Cat(1))
        self.shelter_two.enqueue(Dog(2))
        self.shelter_two.enqueue(Dog(3))
        self.shelter_two.enqueue(Cat(4))
        self.shelter_two.enqueue(Cat(5))
        self.assertIsInstance(self.shelter_two.dequeue_any(), Cat)
        self.assertIsInstance(self.shelter_two.dequeue_dog(), Dog)
        self.assertIsInstance(self.shelter_two.dequeue_any(), Cat)
        self.assertIsInstance(self.shelter_two.dequeue_any(), Dog)

    def test_only_dogs(self):
        for i in range(10):
            self.shelter_one.enqueue(Dog(i))
            self.shelter_two.enqueue(Dog(i))
        self.assertIsNone(self.shelter_one.dequeue_cat())
        self.assertIsNone(self.shelter_two.dequeue_cat())
        for _ in range(5):
            self.assertIsInstance(self.shelter_one.dequeue_dog(), Dog)
            self.assertIsInstance(self.shelter_one.dequeue_any(), Dog)
            self.assertIsInstance(self.shelter_two.dequeue_dog(), Dog)
            self.assertIsInstance(self.shelter_two.dequeue_any(), Dog)

    def test_only_cats(self):
        for i in range(10):
            self.shelter_one.enqueue(Cat(i))
            self.shelter_two.enqueue(Cat(i))
        self.assertIsNone(self.shelter_one.dequeue_dog())
        self.assertIsNone(self.shelter_two.dequeue_dog())
        for _ in range(5):
            self.assertIsInstance(self.shelter_one.dequeue_any(), Cat)
            self.assertIsInstance(self.shelter_one.dequeue_cat(), Cat)
            self.assertIsInstance(self.shelter_two.dequeue_any(), Cat)
            self.assertIsInstance(self.shelter_two.dequeue_cat(), Cat)

    def test_empty(self):
        self.assertIsNone(self.shelter_one.dequeue_cat())
        self.assertIsNone(self.shelter_two.dequeue_cat())
        self.assertIsNone(self.shelter_one.dequeue_dog())
        self.assertIsNone(self.shelter_two.dequeue_dog())
        self.assertIsNone(self.shelter_one.dequeue_any())
        self.assertIsNone(self.shelter_two.dequeue_any())


if __name__ == '__main__':
    unittest.main()
