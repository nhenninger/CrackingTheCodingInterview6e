from nodes import BinaryTreeNode as BTNode


# 4.8   First Common Ancestor
def first_common_ancestor(a: BTNode, b: BTNode, root: BTNode) -> BTNode:
    """
    Find the first common ancestor of two nodes in a binary tree (not
    necessarily a binary search tree).

    Assumes a node is an ancestor of itself.
    Assumes nodes do not have links to parents.
    Assumes nodes are in tree.

    Runtime: O(n)
    Memory: O(n)
    """
    if root is None:
        return None
    elif a == root and b == root:
        return root

    x = first_common_ancestor(a, b, root.left)
    if x is not None and x != a and x != b:
        return x  # Found FCA in left subtree, bubbling it up the call stack

    y = first_common_ancestor(a, b, root.right)
    if y is not None and y != a and y != b:
        return y  # Found FCA in right subtree, bubbling it up the call stack

    if x is not None and y is not None:
        return root  # a and b are on opposite sides of this node; it's the FCA
    elif a == root or b == root:
        return root  # Avoid searching below a or b
    else:
        return x if x is not None else y
