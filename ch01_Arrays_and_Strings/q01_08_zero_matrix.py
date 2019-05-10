# 1.8   Zero Matrix
def zero_matrix(matrix: list, m: int, n: int) -> list:
    """Propagate zero elements to the entire row and column in a matrix.

    If an element in an MxN matrix is zero, its entire row and column are set
    to zero.

    Runtime: O(m*n)
    Memory: O(m+n)
    """
    rows = set()
    columns = set()
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                rows.add(row)
                columns.add(col)
    for row in rows:
        for c in range(n):
            matrix[row][c] = 0
    for col in columns:
        for r in range(m):
            matrix[r][col] = 0
    return matrix


def zero_matrix_constant_memory(matrix: list, m: int, n: int) -> list:
    """Propagate zero elements to the entire row and column in a matrix.

    If an element in an MxN matrix is zero, its entire row and column are set
    to zero.

    Runtime: O(m*n)
    Memory: O(1)
    """
    first_row_has_zero = False
    first_col_has_zero = False
    # Check first row and col before using them to mark internal zeros.
    for col in range(n):
        if matrix[0][col] == 0:
            first_row_has_zero = True
            break
    for row in range(m):
        if matrix[row][0] == 0:
            first_col_has_zero = True
            break

    # Use first row and col to mark internal zeros.
    for row in range(1, m):
        for col in range(1, n):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

    # Propagate internal zeros.
    for col in range(1, n):
        if matrix[0][col] == 0:
            for row in range(1, m):
                matrix[row][col] = 0
    for row in range(1, m):
        if matrix[row][0] == 0:
            for col in range(1, n):
                matrix[row][col] = 0

    # Propagate zeros from first row and first col.
    if first_row_has_zero:
        for col in range(n):
            matrix[0][col] = 0
    if first_col_has_zero:
        for row in range(m):
            matrix[row][0] = 0
    return matrix
