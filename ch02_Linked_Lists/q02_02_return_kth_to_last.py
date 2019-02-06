from linked_list_node import LinkedListNode


# 2.2   Return Kth to Last
def return_kth_to_last(head: LinkedListNode, k: int) -> int:
    """Return the Kth to last element of a singly linked list.

    Runtime: O(n)
    Memory: O(1)
    """
    runner = head
    for _ in range(k):
        runner = runner.next
    while runner.next is not None:
        runner = runner.next
        head = head.next
    return head.data


def return_kth_to_last_recursive(head: LinkedListNode, k: int) -> int:
    """Return the Kth to last element of a singly linked list using recursion.

    Runtime: O(n)
    Memory: O(n)
    """
    node, _ = return_kth_to_last_recursive_helper(head, k)
    return node.data if node is not None else None


def return_kth_to_last_recursive_helper(head: LinkedListNode, k: int) -> tuple:
    if head is None:
        return None, -1  # Off the end!

    target_node, pos = return_kth_to_last_recursive_helper(head.next, k)
    if target_node is not None:  # Keep sending Kth node back to start
        return target_node, pos

    pos += 1
    if pos == k:
        return head, pos

    return None, pos
