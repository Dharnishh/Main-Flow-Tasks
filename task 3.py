def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

def check_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True
    if [board[i][i] for i in range(3)].count(player) == 3 or [board[i][2-i] for i in range(3)].count(player) == 3:
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def best_move(board):
    best_score = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = -1 if check_winner(board, 'X') else 0
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    computer = 'O'

    while True:
        print_board(board)

        if is_board_full(board) or check_winner(board, player) or check_winner(board, computer):
            break

        if player == 'X':
            while True:
                try:
                    row = int(input("Enter row (0, 1, 2): "))
                    col = int(input("Enter column (0, 1, 2): "))
                    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                        board[row][col] = player
                        player = computer
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Please enter a valid number (0, 1, or 2).")
        else:
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = computer
                player = 'X'

    print_board(board)
    if check_winner(board, 'X'):
        print("You win!")
    elif check_winner(board, 'O'):
        print("Computer wins!")
    else:
        print("It's a draw!")

# Run the game
tic_tac_toe()
