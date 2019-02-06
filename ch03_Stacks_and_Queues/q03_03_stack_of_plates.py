# 3.3   Stack of Plates
class SetOfStacks(object):
    """A grouping of stacks.
    """

    def __init__(self, *args, **kwargs):
        self._set = [[]]
        self._threshold = 42

    def push(self, d: int) -> None:
        """Add an element to the grouping.
        """
        top_stack = len(self._set) - 1
        if len(self._set[top_stack]) < self._threshold:
            self._set[top_stack].append(d)
        else:
            self._set.append([d])

    def pop(self) -> int:
        """Remove the most recently added element.
        """
        last_stack = len(self._set) - 1
        if last_stack <= 0 and len(self._set[last_stack]) == 0:
            return None
        temp = self._set[last_stack].pop()
        if len(self._set[last_stack]) == 0:
            self._set.pop()
        return temp

    def pop_at(self, index: int) -> int:
        """Remove the most recently added element from a specific substack.
        """
        if index < 0 or index >= len(self._set):
            raise ValueError("Substack does not exist.")
        return self._set[index].pop()
