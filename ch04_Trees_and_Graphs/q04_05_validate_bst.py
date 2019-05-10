from nodes import BinaryTreeNode


# 4.5   Validate BST
def validate_bst(root: BinaryTreeNode) -> bool:
    """
    Check if a binary tree is a binary search tree.

    Assumes tree contains no duplicates.

    Runtime: O(n)
    Memory: O(n)
    """
    values = []
    _vbst_helper(root, values)
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True


def _vbst_helper(root: BinaryTreeNode, values: list) -> None:
    # In-order traversal
    if root is None:
        return
    _vbst_helper(root.left, values)
    values.append(root.data)
    _vbst_helper(root.right, values)


def validate_bst_no_array(root: BinaryTreeNode) -> bool:
    """
    Check if a binary tree is a binary search tree.

    Assumes tree contains no duplicates.

    Runtime: O(n)
    Memory: O(log n)
    """
    prev = [None]
    return _vbst_no_array_helper(root, prev)


def _vbst_no_array_helper(root: BinaryTreeNode, prev: list) -> bool:
    # In-order traversal
    if root is None:
        return True
    check_left = _vbst_no_array_helper(root.left, prev)

    if prev[0] is not None and root.data < prev[0]:
        return False
    else:
        prev[0] = root.data

    check_right = _vbst_no_array_helper(root.right, prev)
    return check_left and check_right


def validate_bst_allow_dupes(root: BinaryTreeNode) -> bool:
    """
    Check if a binary tree is a binary search tree.

    Duplicates must be in left subtree.

    Runtime: O(n)
    Memory: O(log n)
    """
    return _vbst_allow_dupes_helper(root, None, None)


def _vbst_allow_dupes_helper(root: BinaryTreeNode, floor: int, ceiling: int) -> bool:
    if root is None:
        return True
    # root.data == floor means a duplicate in the right subtree
    if floor is not None and root.data <= floor:
        return False
    if ceiling is not None and root.data > ceiling:
        return False
    return (_vbst_allow_dupes_helper(root.left, floor, root.data)
            and _vbst_allow_dupes_helper(root.right, root.data, ceiling))
