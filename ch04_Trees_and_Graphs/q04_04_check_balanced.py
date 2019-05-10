from nodes import BinaryTreeNode


# 4.4   Check Balanced
def check_balanced(root: BinaryTreeNode) -> bool:
    """
    Check if a binary tree is balanced, i.e., the subtrees of any node always
    have a height difference of zero or one.

    Runtime: O(n)
    Memory: O(n)
    """
    heights = {"min": 0,
               "max": 0}
    check_height(root, heights, 1)
    return -1 <= heights["max"] - heights["min"] <= 1


def check_height(root: BinaryTreeNode, heights: dict, curr_height: int) -> None:
    if root is None:
        if curr_height > heights["max"]:
            heights["max"] = curr_height
        if heights["min"] == 0 or heights["min"] > curr_height:
            heights["min"] = curr_height
        return
    check_height(root.left, heights, curr_height + 1)
    check_height(root.right, heights, curr_height + 1)
