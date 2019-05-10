# 1.7   Rotate Matrix
def rotate_matrix(matrix: list, n: int) -> list:
    """Rotate an NxN matrix 90 degrees counterclockwise.

    Runtime: O(n^2)
    Memory: O(n)
    """
    output = []
    for col in range(n - 1, -1, -1):  # Start at matrix upper left
        new_row = []
        for row in range(n):
            new_row.append(matrix[row][col])
        output.append(new_row)
    return output


# https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
def rotate_matrix_inplace(matrix: list, n: int) -> list:
    """Rotate an NxN matrix 90 degrees counterclockwise in place.

    Runtime: O(n^2)
    Memory: O(1)
    """
    last_index = n - 1
    for layer in range(n // 2):  # From outside layer to inside layer
        layer_len = last_index - layer
        for pos in range(layer, layer_len):
            # save top row
            temp = matrix[layer][pos]
            # top row gets right
            matrix[layer][pos] = matrix[pos][layer_len]
            # right gets bottom
            matrix[pos][layer_len] = matrix[layer_len][last_index - pos]
            # bottom gets left
            matrix[layer_len][last_index - pos] = matrix[last_index - pos][layer]
            # left gets saved top
            matrix[last_index - pos][layer] = temp
    return matrix
