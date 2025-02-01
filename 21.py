def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

matrix1 = [[int(x) for x in input(f"Enter row {i+1} of matrix 1: ").split()] for i in range(2)]
matrix2 = [[int(x) for x in input(f"Enter row {i+1} of matrix 2: ").split()] for i in range(2)]

sum_matrix = add_matrices(matrix1, matrix2)
print("Resultant matrix:")
for row in sum_matrix:
    print(" ".join(map(str, row)))
