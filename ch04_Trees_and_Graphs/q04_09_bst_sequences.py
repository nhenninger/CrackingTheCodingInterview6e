from nodes import BinaryTreeNode as BTNode


# 4.9   BST Sequences
def bst_sequences(root: BTNode) -> list:
    """
    Prints all possible arrays that could produce the given binary search tree

    Assumes tree contains distinct elements.
    Not thread safe.

    Runtime: O(2^n)
    Memory: O(2^n)
    """
    arrays = []
    if root is None:
        arrays.append([])
        return arrays

    prefix = [root.data]
    left_sequence = bst_sequences(root.left)
    right_sequence = bst_sequences(root.right)

    # Weave together
    for left in left_sequence:
        for right in right_sequence:
            weave = []
            _weave_lists(left, right, weave, prefix)
            arrays.extend(weave)

    return arrays


def _weave_lists(first: list, second: list, weave: list, prefix: list) -> None:
    # Remove the head from one list, recurse on it, then do the same for the other list.
    if len(first) == 0 or len(second) == 0:
        clone = prefix.copy()
        clone.extend(first)
        clone.extend(second)
        weave.append(clone)
        return

    head_of_first = first.pop(0)
    prefix.append(head_of_first)
    _weave_lists(first, second, weave, prefix)
    prefix.pop(len(prefix) - 1)
    first.insert(0, head_of_first)

    head_of_second = second.pop(0)
    prefix.append(head_of_second)
    _weave_lists(first, second, weave, prefix)
    prefix.pop(len(prefix) - 1)
    second.insert(0, head_of_second)
