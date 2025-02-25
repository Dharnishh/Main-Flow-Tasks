def is_valid_sudoku(board):
    def is_valid_unit(unit):
        unit = [i for i in unit if i != '.']
        return len(unit) == len(set(unit))
    
    def is_valid_row(board):
        return all(is_valid_unit(row) for row in board)
    
    def is_valid_col(board):
        return all(is_valid_unit(col) for col in zip(*board))
    
    def is_valid_square(board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not is_valid_unit(square):
                    return False
        return True
    
    return is_valid_row(board) and is_valid_col(board) and is_valid_square(board)

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
print(is_valid_sudoku(board))
