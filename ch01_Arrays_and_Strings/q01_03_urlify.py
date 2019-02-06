# 1.3   URLify
def urlify(s: list, n: int) -> list:
    """Replace all spaces in a character list with '%20' without built-in functions.

    Runtime: O(n)
    Memory: O(1)
    """
    tail = len(s) - 1
    for i in range(n - 1, -1, -1):
        if s[i] == ' ':
            s[tail] = '0'
            s[tail - 1] = '2'
            s[tail - 2] = '%'
            tail -= 3
        else:
            s[tail] = s[i]
            tail -= 1
    return s
