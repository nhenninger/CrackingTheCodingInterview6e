from linked_list_node import LinkedListNode


# 2.8   Loop Detection
def loop_detection(head: LinkedListNode) -> LinkedListNode:
    """Return the node at the beginning of a loop in a circular linked list.

    Runtime: O(n)
    Memory: O(n)
    """
    nodes = set()
    while head is not None:
        if head in nodes:
            return head
        else:
            nodes.add(head)
        head = head.next
    return None


def loop_detection_no_buffer(head: LinkedListNode) -> LinkedListNode:
    """Return the node at the beginning of a loop in a circular linked list
    without using a buffer.

    Runtime: O(n)
    Memory: O(1)
    """
    if head is None:
        return head
    tortoise = head
    hare = head.next  # Offset starting position
    found_loop = False
    while hare is not None and hare.next is not None:
        if tortoise is hare:
            found_loop = True
            break
        else:
            tortoise = tortoise.next
            hare = hare.next.next
    if not found_loop:
        return None
    # head to intersection is same length as tortoise to intersection minus
    # offset
    tortoise = tortoise.next
    while head is not tortoise:
        head = head.next
        tortoise = tortoise.next
    return head
