# 3.6   Animal Shelter
class Animal(object):
    """Abstraction of an animal.

    Attributes:
        date: An integer.  Lower numbers entered the shelter before higher.
        next_animal: The next animal in the queue.
    """

    def __init__(self, date: int):
        self.date = date
        self.next_animal = None


class Dog(Animal):
    """Canis familiaris.
    """


class Cat(Animal):
    """Felis catus.
    """


class AnimalShelter(object):
    """Only holds dogs and cats.

    All animals on first in, first out queue.  Adopters may select the first
    dog, the first dog, or the first of all animals.

    Singly linked list version.

    Attributes:
        front: The front of the queue, i.e., the oldest animal.
        tail: The back of the queue, i.e., the most recently admitted animal.
    """

    def __init__(self):
        self.front = None
        self.tail = None

    def enqueue(self, animal: Animal) -> None:
        """Add an animal to the back of the queue.
        """
        if self.front is None and self.tail is None:
            self.front = self.tail = animal
        else:
            self.tail.next_animal = animal
            self.tail = self.tail.next_animal

    def dequeue_any(self) -> Animal:
        """Remove and return the oldest animal (dog or cat) from the queue.
        """
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next_animal
        return temp

    def dequeue_dog(self) -> Dog:
        """Remove and return the oldest dog from the queue.
        """
        if isinstance(self.front, Dog):
            return self.dequeue_any()
        runner = self.front
        while runner is not None and not isinstance(runner.next_animal, Dog):
            runner = runner.next_animal
        if runner is None:
            return None
        found_dog = runner.next_animal
        if found_dog is self.tail:
            self.tail = runner
        runner.next_animal = found_dog.next_animal
        return found_dog

    def dequeue_cat(self) -> Cat:
        """Remove and return the oldest cat from the queue.
        """
        if isinstance(self.front, Cat):
            return self.dequeue_any()
        runner = self.front
        while runner is not None and not isinstance(runner.next_animal, Cat):
            runner = runner.next_animal
        if runner is None:
            return None
        found_cat = runner.next_animal
        if found_cat is self.tail:
            self.tail = runner
        runner.next_animal = found_cat.next_animal
        return found_cat


class AnimalShelterTwoLists(object):
    """Only holds dogs and cats.

    All animals on first in, first out queue.  Adopters may select the first
    dog, the first dog, or the first of all animals.

    Separate linked lists version.

    Attributes:
        oldest_cat: The cat at the front of the cat queue.
        newest_cat: The cat at the end of the cat queue.
        oldest_dog: The dog at the front of the dog queue.
        newest_dog: The dog at the end of the dog queue.
    """

    def __init__(self):
        self.oldest_cat = None
        self.newest_cat = None
        self.oldest_dog = None
        self.newest_dog = None

    def enqueue(self, animal: Animal) -> None:
        """Add an animal to the back of the queue.
        """
        if isinstance(animal, Cat):
            if self.oldest_cat is None:
                self.oldest_cat = animal
                self.newest_cat = animal
            else:
                self.newest_cat.next_animal = animal
                self.newest_cat = animal
        elif isinstance(animal, Dog):
            if self.oldest_dog is None:
                self.oldest_dog = animal
                self.newest_dog = animal
            else:
                self.newest_dog.next_animal = animal
                self.newest_dog = animal
        else:
            raise TypeError()

    def dequeue_any(self) -> Animal:
        """Remove and return the oldest animal (dog or cat) from the queue.
        """
        if self.oldest_dog is not None and self.oldest_cat is not None:
            if self.oldest_cat.date < self.oldest_dog.date:
                return self.dequeue_cat()
        elif self.oldest_cat is not None:
            return self.dequeue_cat()
        return self.dequeue_dog()

    def dequeue_dog(self) -> Dog:
        """Remove and return the oldest dog from the queue.
        """
        dog = self.oldest_dog
        if dog is None:
            return None
        else:
            self.oldest_dog = self.oldest_dog.next_animal
        return dog

    def dequeue_cat(self) -> Cat:
        """Remove and return the oldest cat from the queue.
        """
        cat = self.oldest_cat
        if cat is None:
            return None
        else:
            self.oldest_cat = self.oldest_cat.next_animal
        return cat
