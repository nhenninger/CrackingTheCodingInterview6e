from collections import defaultdict


# 1.2   Check Permutation
def check_permutation(a: str, b: str) -> bool:
    """Determine if two strings are permutations of each other.

    Sensitive to character case, whitespace, and punctuation.

    Runtime: O(a+b)
    Memory: O(a+b)
    """
    chars = defaultdict(int)
    for ch in a:
        chars[ch] += 1
    for ch in b:
        if ch not in chars:
            return False
        elif chars[ch] > 1:
            chars[ch] -= 1
        else:
            del chars[ch]
    return len(chars) == 0
