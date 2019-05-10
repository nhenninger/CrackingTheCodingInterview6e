class Node(object):
    """A very basic node.

    Attributes:
        data: An integer
    """

    def __init__(self, d: int) -> None:
        self.data = d

    def visit(self) -> None:
        """Print the data."""
        print(self.data)


class BinaryTreeNode(Node):
    """A very basic node in a binary tree.

    Attributes:
        left: The left child
        right: The right child
    """

    def __init__(self, d: int) -> None:
        super().__init__(d)
        self.left = None
        self.right = None


class LinkedListNode(object):
    """A very basic node in a singly-linked list.

    Attributes:
        next: The next node in the list
    """

    def __init__(self, btn: BinaryTreeNode) -> None:
        self.btn = btn
        self.next = None


class LinkedList(object):
    """A very basic singly-linked list.

    Attributes:
        head: The head node.
        size: The length of the list.
    """

    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def add_node(self, node: LinkedListNode) -> LinkedListNode:
        """Add a node to the tail of the list."""
        if self.head is None:
            self.head = node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = node
        self.size += 1
        return self.head

    def add_int(self, d: int) -> None:
        """Create a new node at the tail of the list"""
        node = LinkedListNode(d)
        self.add_node(node)


class GraphNode(Node):
    """A very basic node in a graph.
    
    Attributes:
        children: A list of child nodes
        marked: Whether this node has been visited before
    """

    def __init__(self, d: int) -> None:
        super().__init__(d)
        self.children = []
        self.marked = False
