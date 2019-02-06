# 3.2   Stack Min
class StackMinNode(object):
    """A singly linked list node for use in a StackMin.

    Attributes:
        data: An integer
        next: The next node in the stack.
        prev_min: The previously minimum node.
    """

    def __init__(self, d: int):
        self.data = d
        self.next = None
        self.prev_min = None


class StackMin(object):
    """An enhanced stack.
    """

    def __init__(self, *args, **kwargs):
        self._top = None
        self._min = None

    def push(self, d: int) -> None:
        """Add an element to the top of the stack.
        """
        node = StackMinNode(d)
        if self._top is None:
            self._top = node
            self._min = node
        else:
            node.next = self._top
            self._top = node
            if node.data < self._min.data:
                node.prev_min = self._min
                self._min = node

    def pop(self) -> StackMinNode:
        """Remove a node from the top of the stack.
        """
        if self._top is None:
            return None
        if self._min is self._top:
            self._min = self._min.prev_min
        temp = self._top
        self._top = self._top.next
        return temp

    def minimum(self) -> int:
        """Return the value of the minimum element.
        """
        if self._min is None:
            return None
        return self._min.data
