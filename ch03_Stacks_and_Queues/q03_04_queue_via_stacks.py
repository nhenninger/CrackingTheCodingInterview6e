# 3.4   Queue via Stacks
class MyQueue(object):
    """A custom queue composed of two stacks.
    """

    def __init__(self) -> None:
        self._stack_A = []
        self._stack_B = []

    def push(self, d: int) -> None:
        """Add an element to the end of the queue.
        """
        while len(self._stack_A) > 0:
            x = self._stack_A.pop()
            self._stack_B.append(x)
        self._stack_A.append(d)
        while len(self._stack_B) > 0:
            y = self._stack_B.pop()
            self._stack_A.append(y)

    def pop(self) -> int:
        """Remove an element from the front of the queue.
        """
        return self._stack_A.pop()
