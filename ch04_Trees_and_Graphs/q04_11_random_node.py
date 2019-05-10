from nodes import BinaryTreeNode
from random import randint


# 4.11   Random Node
class BinarySearchTreeNode(BinaryTreeNode):
    """A very basic node in a binary tree.
    Insert, find, and delete functionality shamelessly modeled from code at
    https://en.wikipedia.org/wiki/Binary_search_tree

    Attributes:
        parent: The parent node
        size: The number of nodes in this subtree, beginning at 1.
    """

    def __init__(self, d: int, parent: 'BinarySearchTreeNode'):
        super().__init__(d)
        self.parent = parent
        self.size = 1

    def insert(self, d: int) -> 'BinarySearchTreeNode':
        """
        Insert a value into the tree.  Duplicates permitted.
        :param d: The new value.
        :return: The newly created node.
        """
        self.size += 1
        if d <= self.data:
            if self.left is None:
                self.left = BinarySearchTreeNode(d, self)
                return self.left
            else:
                self.left.insert(d)
        else:
            if self.right is None:
                self.right = BinarySearchTreeNode(d, self)
            else:
                self.right.insert(d)
                return self.right

    def find(self, d: int) -> 'BinarySearchTreeNode':
        """
        Locate a node in the tree.
        :param d: The value to find.
        :return: The first node containing the value or None if not found.
        """
        curr = self
        while curr is not None:
            if d == curr.data:
                return curr
            elif d < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def __find_min(self):
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr

    def __replace_node_in_parent(self, replacement: 'BinarySearchTreeNode' = None):
        if self.parent is not None:
            if self is self.parent.left:
                self.parent.left = replacement
            else:
                self.parent.right = replacement
        if replacement is not None:
            replacement.parent = self.parent

    def delete(self, d: int):
        """
        Remove a value from the tree.
        :param d: The value to remove.
        """
        self.size -= 1
        if d < self.data:
            return self.left.delete(d)
        elif d > self.data:
            return self.right.delete(d)

        if self.left is not None and self.right is not None:
            successor = self.right.__find_min()
            self.data = successor.data
            successor.delete(successor.data)
        elif self.left is not None:
            self.__replace_node_in_parent(self.left)
        elif self.right is not None:
            self.__replace_node_in_parent(self.right)
        else:
            self.__replace_node_in_parent(None)

    def get_random_node(self) -> 'BinarySearchTreeNode':
        """
        Return a random node in the tree.

        Runtime: O(log n)
        Memory: O(log n)
        """
        if self.left is None and self.right is None:
            return self
        rand = randint(1, self.size)
        if self.left is None:
            return self if rand == 1 else self.right.get_random_node()
        elif self.right is None:
            return self if rand == self.size else self.left.get_random_node()
        else:
            if rand <= self.left.size:
                return self.left.get_random_node()
            elif rand > self.left.size + 1:
                return self.right.get_random_node()
            else:
                return self
