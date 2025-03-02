def is_valid_sudoku(board):
    for i in range(9):
        row = []
        col = []
        box = []
        for j in range(9):
            # Check row
            if board[i][j] != '.':
                if board[i][j] in row:
                    return False
                row.append(board[i][j])
            # Check column
            if board[j][i] != '.':
                if board[j][i] in col:
                    return False
                col.append(board[j][i])
            # Check 3x3 box
            box_row = 3 * (i // 3) + j // 3
            box_col = 3 * (i % 3) + j % 3
            if board[box_row][box_col] != '.':
                if board[box_row][box_col] in box:
                    return False
                box.append(board[box_row][box_col])
    return True

# Example usage
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print("Is Sudoku Valid?", is_valid_sudoku(board))