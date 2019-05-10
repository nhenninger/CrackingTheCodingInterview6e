from nodes import BinaryTreeNode as BTNode


# 4.10   Check Subtree
def check_subtree(root_a: BTNode, root_b: BTNode) -> bool:
    """
    Check if tree B is a subtree of tree A.

    I.e., tree A has node N such that the subtree of N is identical to tree B.

    Runtime: O(n + km) where k is the number of nodes in tree A matching root_b
    Memory: O(log n + log m)
    """
    if root_a is None or root_b is None:
        return False
    if root_a.data == root_b.data and _cs_helper(root_a, root_b):
        return True
    else:
        return check_subtree(root_a.left, root_b) or check_subtree(root_a.right, root_b)


def _cs_helper(node_a: BTNode, node_b: BTNode) -> bool:
    if node_a is None and node_b is None:
        return True
    elif node_a is None and node_b is not None:
        return False
    elif node_b is None and node_a is not None:
        return False
    elif node_a.data != node_b.data:
        return False
    else:
        return (_cs_helper(node_a.left, node_b.left)
                and _cs_helper(node_a.right, node_b.right))
