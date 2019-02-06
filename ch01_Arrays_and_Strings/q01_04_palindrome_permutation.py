# 1.4   Palindrome Permutation
def palindrome_permutation(s: str) -> bool:
    """Check if a string is a permutation of a palindrome.

    Ignores case, numbers, whitespace, and punctuation.

    Runtime: O(n)
    Memory: O(n)
    """
    chars = {}
    s = s.lower()
    for ch in s:
        if not ch.isalpha():
            continue
        elif ch in chars:
            del chars[ch]
        else:
            chars[ch] = ch
    return 0 <= len(chars) <= 1


def palindrome_permutation_bit_vector(s: str) -> bool:
    """Check if a string is a permutation of a palindrome using a bit vector.

    Ignores case, numbers, whitespace, and punctuation.

    Runtime: O(n)
    Memory: O(n)
    """
    bits = 0
    s = s.lower()
    for ch in s:
        if not ch.isalpha():
            continue

        b = 1 << ord(ch)
        if b & bits == b:
            bits -= b
        else:
            bits += b
    return bits & (bits - 1) == 0
