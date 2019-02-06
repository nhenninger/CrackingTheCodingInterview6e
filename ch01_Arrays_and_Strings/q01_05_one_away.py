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
        for i in range(len(a)):
            if a[i] != b[i] and found_diff:
                return False
            elif a[i] != b[i]:
                found_diff = True
    else:  # Insert/remove char
        big_arr = a if len(a) > len(b) else b
        short_arr = b if len(a) > len(b) else a
        big_i = 0
        for i in range(len(short_arr)):
            if short_arr[i] != big_arr[big_i] and big_i - i == 1:
                return False
            elif short_arr[i] != big_arr[big_i]:
                big_i += 2
            else:
                big_i += 1
    return True
