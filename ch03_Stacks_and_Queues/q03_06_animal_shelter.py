# 3.6   Animal Shelter
class Animal(object):
    """Abstraction of an animal.

    Attributes:
        date: An integer.  Lower numbers entered the shelter before higher.
        next: The next animal in the queue.
    """

    def __init__(self, date: int):
        self.date = date
        self.next = None


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
    """

    def __init__(self):
        self._head = None
        self._tail = None

    def enqueue(self, animal: Animal) -> None:
        """Add an animal to the back of the queue.
        """
        if self._head is None and self._tail is None:
            self._head = self._tail = animal
        else:
            self._tail.next = animal
            self._tail = animal

    def dequeue_any(self) -> Animal:
        """Remove and return the oldest animal (dog or cat) from the queue.
        """
        if self._head is None:
            return None
        temp = self._head
        self._head = self._head.next
        return temp

    def dequeue_dog(self) -> Dog:
        """Remove and return the oldest dog from the queue.
        """
        found_dog = self._dequeue_type(Dog)
        assert (found_dog is None or isinstance(found_dog, Dog))
        return found_dog

    def dequeue_cat(self) -> Cat:
        """Remove and return the oldest cat from the queue.
        """
        found_cat = self._dequeue_type(Cat)
        assert (found_cat is None or isinstance(found_cat, Cat))
        return found_cat

    def _dequeue_type(self, pet_type: type) -> Animal:
        if isinstance(self._head, pet_type):
            return self.dequeue_any()

        runner = self._head
        while runner is not None and not isinstance(runner.next, pet_type):
            runner = runner.next
        if runner is None:  # End of queue
            return None
        found = runner.next
        if found is self._tail:
            self._tail = runner
            self._tail.next = None
        else:
            runner.next = found.next
        return found


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
                self.newest_cat.next = animal
                self.newest_cat = animal
        elif isinstance(animal, Dog):
            if self.oldest_dog is None:
                self.oldest_dog = animal
                self.newest_dog = animal
            else:
                self.newest_dog.next = animal
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
        if self.oldest_dog is None:
            return None
        else:
            dog = self.oldest_dog
            self.oldest_dog = self.oldest_dog.next
            return dog

    def dequeue_cat(self) -> Cat:
        """Remove and return the oldest cat from the queue.
        """
        if self.oldest_cat is None:
            return None
        else:
            cat = self.oldest_cat
            self.oldest_cat = self.oldest_cat.next
            return cat
