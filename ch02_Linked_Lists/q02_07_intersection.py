from linked_list_node import LinkedListNode


# 2.7   Intersection
def intersection(a: LinkedListNode, b: LinkedListNode) -> LinkedListNode:
    """Check if two linked lists intersect.

    An intersection is defined by reference.  If the Kth node of a list is the
    exact same node (by reference) as the Jth node of another list, then they
    are intersecting.

    Runtime: O(n^2)
    Memory: O(n)
    """
    nodes = []
    while a is not None:
        nodes.append(a)
        a = a.next
    while b is not None:
        if b in nodes:
            return b
        b = b.next
    return None


def intersection_no_buffer(a: LinkedListNode, b: LinkedListNode) -> LinkedListNode:
    """Check if two linked lists intersect without a buffer.

    An intersection is defined by reference.  If the Kth node of a list is the
    exact same node (by reference) as the Jth node of another list, then they
    are intersecting.

    Runtime: O(n)
    Memory: O(1)
    """
    runner_a = a
    runner_b = b
    length_a = length_b = 0
    while runner_a is not None:
        length_a += 1
        runner_a = runner_a.next
    while runner_b is not None:
        length_b += 1
        runner_b = runner_b.next
    if runner_a is not runner_b:
        return None

    if length_a > length_b:
        for _ in range(length_a - length_b):
            a = a.next
    elif length_b > length_a:
        for _ in range(length_b - length_a):
            b = b.next

    while a is not b:
        a = a.next
        b = b.next
    return a
