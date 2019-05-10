from nodes import BinaryTreeNode, LinkedList, LinkedListNode as LLNode


# 4.3   List of Depths
def list_of_depths_dfs(root: BinaryTreeNode) -> dict:
    """
    Creates a dictionary of linked lists.  Each list contains all the nodes at
    each depth of the tree.

    Runtime: O(n)
    Memory: O(n)
    """
    lists = {}
    _lod_dfs_helper(root, 0, lists)
    return lists


def _lod_dfs_helper(root: BinaryTreeNode, depth: int, lists: dict) -> None:
    # Fundamentally a pre-order traversal.
    if root is None:
        return
    if depth not in lists:
        lists[depth] = LinkedList()
    lists[depth].add_node(LLNode(root))
    _lod_dfs_helper(root.left, depth + 1, lists)
    _lod_dfs_helper(root.right, depth + 1, lists)


def list_of_depths_bfs(root: BinaryTreeNode) -> dict:
    """
    Creates a dictionary of linked lists.  Each list contains all the nodes at
    each depth of the tree.

    Runtime: O(n)
    Memory: O(n)
    """
    # Fundamentally a breadth-first search.
    if root is None:
        return
    lists = {}
    depth = 0
    curr_row = LinkedList()
    curr_row.add_node(LLNode(root))
    while curr_row.size > 0:
        lists[depth] = curr_row  # Stash results of previous level
        depth += 1
        parents = curr_row
        curr_row = LinkedList()
        p_head = parents.head
        while p_head is not None:
            if p_head.btn.left is not None:
                l_child = LLNode(p_head.btn.left)
                curr_row.add_node(l_child)
            if p_head.btn.right is not None:
                r_child = LLNode(p_head.btn.right)
                curr_row.add_node(r_child)
            p_head = p_head.next
    return lists
