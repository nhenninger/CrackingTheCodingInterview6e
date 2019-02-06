# 1.6   String Compression
def string_compression(s: str) -> str:
    """Perform rudimentary string compression.

    Shortens repeated characters into the character followed by its count.

    Runtime: O(n)
    Memory: O(n)
    """
    chars = []
    i = 0
    while i < len(s):
        j = 1
        while i + j < len(s) and s[i + j] == s[i]:
            j += 1
        chars.append(s[i])
        chars.append(str(j))
        i += j
    if len(chars) >= len(s):
        return s
    else:
        return ''.join(chars)
