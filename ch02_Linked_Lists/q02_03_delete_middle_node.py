from linked_list_node import LinkedListNode


# 2.3   Delete Middle Node
def delete_middle_node(node: LinkedListNode) -> None:
    """Delete a node from anywhere in the middle of a singly linked list.

    Runtime: O(n)
    Memory: O(1)
    """
    while node.next.next is not None:
        node.data = node.next.data
        node = node.next
    node.data = node.next.data
    node.next = None
