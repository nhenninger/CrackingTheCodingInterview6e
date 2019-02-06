# 1.9   String Rotation
def string_rotation(a: str, b: str) -> bool:
    """Check if two strings are rotations of each other.

    Runtime: O(n)
    Memory: O(n)
    """
    if len(a) != len(b):
        return False
    return a in b * 2  # isSubstring(b, a + a)
