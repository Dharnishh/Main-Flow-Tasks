def rotate_matrix(matrix):
    # Transpose the matrix
    transposed_matrix = list(zip(*matrix))
    # Reverse each row
    rotated_matrix = [list(reversed(row)) for row in transposed_matrix]
    return rotated_matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotate_matrix(matrix))
