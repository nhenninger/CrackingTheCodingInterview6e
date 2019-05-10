from nodes import BinaryTreeNode


# 4.2   Minimal Tree
def minimal_tree(arr: list) -> BinaryTreeNode:
    """
    Create a binary search tree with minimal height from a sorted array of
    unique integers.

    Runtime: O(n)
    Memory: O(n)
    """
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return BinaryTreeNode(arr[0])
    middle = len(arr) // 2
    root = BinaryTreeNode(arr[middle])
    root.left = minimal_tree(arr[:middle])
    root.right = minimal_tree(arr[middle + 1:len(arr) - 1])
    return root
