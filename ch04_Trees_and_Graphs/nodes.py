class BinaryTreeNode(object):
    """A very basic node in a binary tree."""

    def __init__(self, d: int) -> None:
        """Initialize a new node in the tree."""
        self.data = d
        self.left = None
        self.right = None

    def visit(self) -> None:
        """Print the data."""
        print(self.data)


class GraphNode(object):
    """A very basic node in a graph.
    
    Attributes:
        data: An integer
        children: A list of child nodes
        marked: Whether this node has been visited before
    """

    def __init__(self, d: int) -> None:
        """Initialize a new node in the graph."""
        self.data = d
        self.children = []
        self.marked = False

    def visit(self) -> None:
        """Print the data."""
        print(self.data)
