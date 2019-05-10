from nodes import BinaryTreeNode as BTNode


# 4.12   Paths With Sum
def paths_with_sum(root: BTNode, target_sum: int) -> int:
    """
    Count the paths in a tree which results in a given integer sum.

    Paths must be contiguous and flow only down the tree.  They need not start
    or end on the root or leaves.

    Nodes may contain any integer value.

    :param root: The root of the tree
    :param target_sum: The targeted sum
    :return: The number of paths

    Runtime: O(n)
    Memory: O(n)
    """
    return _pws_helper(root, target_sum, 0, {})


def _pws_helper(root: BTNode, target_sum: int, running_sum: int, paths: dict) -> int:
    if root is None:
        return 0

    running_sum += root.data
    num_paths = paths.get(running_sum - target_sum, 0)

    if running_sum == target_sum:
        num_paths += 1

    _increment_hash_table(paths, running_sum)
    num_paths += _pws_helper(root.left, target_sum, running_sum, paths)
    num_paths += _pws_helper(root.right, target_sum, running_sum, paths)
    _decrement_hash_table(paths, running_sum)

    return num_paths


def _increment_hash_table(table: dict, key: int) -> None:
    if key in table:
        table[key] += 1
    else:
        table[key] = 1


def _decrement_hash_table(table: dict, key: int) -> None:
    if key not in table:
        return
    elif table[key] == 1:
        del table[key]
    else:
        table[key] -= 1
