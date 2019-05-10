from collections import deque
from linked_list_node import LinkedListNode


# 2.6   Palindrome
def palindrome(head: LinkedListNode) -> bool:
    """Check if a linked list is a palindrome.

    Ignores punctuation, whitespace, and case.

    Runtime: O(n)
    Memory: O(n)
    """
    chars = deque([])
    while head is not None:
        ch = chr(head.data)
        if ch.isalpha():
            chars.append(ch.lower())
        head = head.next
    while len(chars) >= 2:
        if chars.pop() != chars.popleft():
            return False
    return True


def palindrome_reverse_list(head: LinkedListNode) -> bool:
    """Check if a linked list is a palindrome.

    Ignores punctuation, whitespace, and case.

    Runtime: O(n)
    Memory: O(n)
    """
    reverse_list = LinkedListNode(head.data)
    runner = head.next
    while runner is not None:
        new_node = LinkedListNode(runner.data)
        new_node.next = reverse_list
        reverse_list = new_node
        runner = runner.next

    while head is not None:
        h = chr(head.data)
        r = chr(reverse_list.data)
        if not h.isalpha():
            head = head.next
        elif not r.isalpha():
            reverse_list = reverse_list.next
        elif h.lower() != r.lower():
            return False
        else:
            head = head.next
            reverse_list = reverse_list.next
    return True


def palindrome_recursive(head: LinkedListNode, length: int) -> bool:
    """Check if a linked list is a palindrome.

    Punctuation and whitespace sensitive.
    Case insensitive

    Runtime: O(n)
    Memory: O(n)
    """
    if length == 1:
        return True
    elif length == 2:
        return head.data == head.next.data
    runner = head
    for _ in range(length - 1):
        runner = runner.next
    h = chr(head.data).lower()
    r = chr(runner.data).lower()
    return h == r and palindrome_recursive(head.next, length - 2)
