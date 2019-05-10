from linked_list_node import LinkedListNode


# 2.5   Sum Lists
def sum_lists_reverse(a: LinkedListNode,
                      b: LinkedListNode) -> LinkedListNode:
    """Add two integers stored as a linked list.

    Each digit of the integer is a node, and the 1's place is the head node.

    Runtime: O(n)
    Memory: O(1)
    """
    carry = 0
    head = curr = None
    while a is not None or b is not None or carry == 1:
        x = 0 if a is None else a.data
        y = 0 if b is None else b.data
        if a is not None:
            a = a.next
        if b is not None:
            b = b.next

        digit = x + y + carry
        carry = digit // 10
        digit %= 10
        if head is None:
            head = LinkedListNode(digit)
            curr = head
        else:
            curr.next = LinkedListNode(digit)
            curr = curr.next
    return head


def sum_lists_reverse_recursive(a: LinkedListNode,
                                b: LinkedListNode,
                                carry: int = 0) -> LinkedListNode:
    """Add two integers stored as a linked list without intermediate conversion.

    Each digit of the integer is a node, and the 1's place is the head node.

    Runtime: O(n)
    Memory: O(n)
    """
    if a is None and b is None:
        return None
    x = 0 if a is None else a.data
    y = 0 if b is None else b.data
    digit = x + y + carry
    carry = digit // 10
    digit %= 10
    head = LinkedListNode(digit)
    if a is not None:
        a = a.next
    if b is not None:
        b = b.next
    head.next = sum_lists_reverse_recursive(a, b, carry)
    return head


def sum_lists_forward(a: LinkedListNode,
                      b: LinkedListNode) -> LinkedListNode:
    """Add two integers stored as a linked list.

    Each digit of the integer is a node, and the 1's place is the tail.

    Runtime: O(n)
    Memory: O(1)
    """
    x = y = 0
    while a is not None:  # Could refactor to another function
        x += a.data
        if a.next is not None:
            x *= 10
        a = a.next
    while b is not None:
        y += b.data
        if b.next is not None:
            y *= 10
        b = b.next
    total = x + y
    head = None
    while total > 0:
        digit = total % 10
        total = total // 10
        curr = LinkedListNode(digit)
        if head is None:
            head = curr
        else:
            curr.next = head
            head = curr
    return head


def sum_lists_forward_stack(a: LinkedListNode,
                            b: LinkedListNode) -> LinkedListNode:
    """Add two integers stored as a linked list using a stack.

    Each digit of the integer is a node, and the 1's place is the tail.

    Runtime: O(n)
    Memory: O(n)
    """
    stack_a = []
    stack_b = []
    while a is not None:
        stack_a.append(a.data)
        a = a.next
    while b is not None:
        stack_b.append(b.data)
        b = b.next
    head = None
    carry = 0
    while len(stack_a) > 0 or len(stack_b) > 0 or carry == 1:
        x = stack_a.pop() if len(stack_a) > 0 else 0
        y = stack_b.pop() if len(stack_b) > 0 else 0
        digit = x + y + carry
        carry = digit // 10
        digit %= 10
        curr = LinkedListNode(digit)
        if head is None:
            head = curr
        else:
            curr.next = head
            head = curr
    return head


def sum_lists_forward_recursive(a: LinkedListNode,
                                b: LinkedListNode) -> LinkedListNode:
    """Add two integers stored as a linked list using recursion.

    Each digit of the integer is a node, and the 1's place is the tail.

    Runtime: O(n)
    Memory: O(n)
    """
    curr_a, curr_b = a, b
    len_a = len_b = 0
    while curr_a is not None:
        len_a += 1
        curr_a = curr_a.next
    while curr_b is not None:
        len_b += 1
        curr_b = curr_b.next
    if len_a > len_b:
        b = pad_zeroes(b, len_a - len_b)
    elif len_b > len_a:
        a = pad_zeroes(a, len_b - len_a)
    head, carry = sum_lists_forward_recursive_helper(a, b)
    if carry > 0:
        curr = LinkedListNode(1)
        curr.next = head
        head = curr
    return head


def pad_zeroes(node: LinkedListNode, n: int) -> LinkedListNode:
    for _ in range(n):
        new_node = LinkedListNode(0)
        new_node.next = node
        node = new_node
    return node


def sum_lists_forward_recursive_helper(a: LinkedListNode,
                                       b: LinkedListNode) -> (LinkedListNode, int):
    if a.next is None and b.next is None:
        digit = a.data + b.data
        carry = digit // 10
        digit %= 10
        curr = LinkedListNode(digit)
        return curr, carry
    next_node, carry = sum_lists_forward_recursive_helper(a.next, b.next)
    digit = a.data + b.data + carry
    carry = digit // 10
    digit %= 10
    curr = LinkedListNode(digit)
    curr.next = next_node
    return curr, carry
