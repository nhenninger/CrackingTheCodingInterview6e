# 1.5   One Away
def one_away(a: str, b: str) -> bool:
    """Check if two strings have one or zero edits of difference.

    An edit is an insertion, a removal, or a replacement of a character.

    Runtime: O(n)
    Memory: O(1)
    """
    if abs(len(a) - len(b)) > 1:  # More than one edit of difference
        return False
    elif len(a) == len(b):  # Replacing char
        found_diff = False
        for i, ch in enumerate(a):
            if ch != b[i] and found_diff:
                return False
            elif ch != b[i]:
                found_diff = True
    else:  # Insert/remove char
        big = a if len(a) > len(b) else b
        small = b if len(a) > len(b) else a
        j = 0
        for i, ch in enumerate(small):
            if ch != big[j] and j - i == 1:
                return False
            elif ch != big[j]:
                j += 2
            else:
                j += 1
    return True
