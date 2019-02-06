from linked_list_node import LinkedListNode


# 2.1   Remove Dups
def remove_dups(n: LinkedListNode) -> None:
    """Remove duplicates from an unsorted singly linked list.

    Runtime: O(n)
    Memory: O(n)
    """
    uniques = {n.data}
    while n is not None and n.next is not None:
        if n.next.data in uniques:
            n.next = n.next.next
        else:
            uniques.add(n.next.data)
            n = n.next


def remove_dups_no_buffer(n: LinkedListNode) -> None:
    """Remove duplicates from an unsorted singly linked list without a buffer.

    Runtime: O(n^2)
    Memory: O(1)
    """
    while n is not None and n.next is not None:
        runner = n
        while runner is not None and runner.next is not None:
            if runner.next.data == n.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        n = n.next
