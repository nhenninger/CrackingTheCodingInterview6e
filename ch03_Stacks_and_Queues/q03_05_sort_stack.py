# 3.5   Sort Stack
def sort_stack(stack: list) -> list:
    """Sort a stack to place the smallest elements on top.

    Runtime: O(n^2)
    Memory: O(n)
    """
    temp_stack = []
    while len(stack) > 0:
        d = stack.pop()
        count = 0
        while len(temp_stack) > 0 and d < temp_stack[len(temp_stack) - 1]:
            count += 1
            stack.append(temp_stack.pop())
        temp_stack.append(d)
        for _ in range(count):
            temp_stack.append(stack.pop())
    while len(temp_stack) > 0:
        stack.append(temp_stack.pop())
    return stack
