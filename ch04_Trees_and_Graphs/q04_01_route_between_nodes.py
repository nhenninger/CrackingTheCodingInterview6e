from nodes import GraphNode
from queue import Queue


# 4.1   Route Between Nodes
def route_between_nodes_dfs(a: GraphNode, b: GraphNode) -> bool:
    """
    Determine whether a route exists between two nodes in a directed graph.

    Runtime: varies
    Memory: varies
    """
    if a is None or b is None:
        return False
    return _rbn_dfs_helper(a, b)


def _rbn_dfs_helper(node: GraphNode, end: GraphNode) -> bool:
    if node is end:
        return True
    node.marked = True
    for child in node.children:
        if not child.marked:
            if _rbn_dfs_helper(child, end):
                return True
    return False


def route_between_nodes_bfs(a: GraphNode, b: GraphNode) -> bool:
    """
    Determine whether a route exists between two nodes in a directed graph.

    Runtime: varies
    Memory: varies
    """
    if a is None or b is None:
        return False
    return _rbn_bfs_helper(a, b)


def _rbn_bfs_helper(root: GraphNode, end: GraphNode) -> bool:
    q = Queue()
    root.marked = True
    q.put(root)
    while not q.empty():
        node = q.get()
        if node is end:
            return True
        for child in node.children:
            if not child.marked:
                child.marked = True
                q.put(child)
    return False
