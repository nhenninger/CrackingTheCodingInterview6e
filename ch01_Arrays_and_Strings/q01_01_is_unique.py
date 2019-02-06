# 1.1   Is Unique
def is_unique(s: str) -> bool:
    """Determine if a string has all unique characters.

    Runtime: O(n)
    Memory: O(n)
    """
    chars = {}
    for ch in s:
        if ch in chars:
            return False
        else:
            chars[ch] = ch
    return True


def is_unique_bit_vector(s: str) -> bool:
    """Determine if a string has all unique characters with a bit vector.

    Uses 1/8th memory of is_unique() but assumes string contains only ASCII
    characters.

    Runtime: O(n)
    Memory: O(n)
    """
    bits = 0
    for ch in s:
        b = 1 << ord(ch)
        if b & bits == b:
            return False
        else:
            bits += b
    return True


def is_unique_no_data_structures(s: str) -> bool:
    """Determine if a string has all unique characters without additional data
    structures.

    Runtime: O(n^2)
    Memory: O(1)
    """
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


def is_unique_sorted(s: str) -> bool:
    """Determine if a string has all unique characters by sorting them.

    Runtime: O(n * log N)
    Memory: O(1)
    """
    s = sorted(s)
    for i in range(len(s) - 2):
        if s[i] == s[i + 1]:
            return False
    return True
