from linked_list_node import LinkedListNode


# 2.4   Partition
def partition(head: LinkedListNode, x: int) -> LinkedListNode:
    """Partition a singly linked list around a value x.

    All nodes less than x come before nodes greater than or equal to x.  The
    partition element x can appear anywhere in second grouping.

    Runtime: O(n)
    Memory: O(n)
    """
    new_head = left_tail = None
    right_curr = head
    right_prev = None
    while right_curr is not None:
        d = right_curr.data
        if d < x:
            if new_head is None:
                new_head = left_tail = LinkedListNode(d)
            else:
                left_tail.next = LinkedListNode(d)
                left_tail = left_tail.next

            if right_prev is None:  # i.e., haven't found anything >= x
                head = right_curr = right_curr.next
            else:
                right_prev.next = right_curr.next
                right_curr = right_curr.next
        else:
            right_prev = right_curr
            right_curr = right_curr.next
    left_tail.next = head
    return new_head
