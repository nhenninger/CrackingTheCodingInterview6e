# 3.1   Three in One
def three_in_one(size: int) -> tuple:
    """Implement three stacks in a single array/list.

    Runtime: O(n)
    Memory: O(n)
    """
    arr = [i for i in range(size)]
    one_third = size // 3
    a = arr[0:one_third]
    b = arr[one_third: 2 * one_third]
    c = arr[2 * one_third:size]
    return a, b, c
