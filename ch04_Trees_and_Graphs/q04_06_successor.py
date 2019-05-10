from nodes import BinaryTreeNode


# 4.6   Successor
class SuccessorNode(BinaryTreeNode):
    """A node with a link to its parent.

    Attributes:
        parent: The parent node.
    """

    def __init__(self, d, parent=None):
        super().__init__(d)
        self.parent = parent


def successor(node: SuccessorNode) -> SuccessorNode:
    """
    Find the in-order successor of a given binary search tree node.

    Nodes must have references to parent.

    Runtime: O(n)
    Memory: O(log n)
    """
    if node is None:
        return node
    if node.right is None:
        node = _walk_up_right(node)
        if node.parent is not None:  # Reached successor
            return node.parent
        else:
            return None  # No successor
    return _in_order_traversal(node.right)


def _walk_up_right(node: SuccessorNode) -> SuccessorNode:
    while node.parent is not None and node.data > node.parent.data:
        node = node.parent
    return node


def _in_order_traversal(node: SuccessorNode) -> SuccessorNode:
    if node.left is not None:
        return _in_order_traversal(node.left)
    return node
