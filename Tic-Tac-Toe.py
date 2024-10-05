'''Tic-Tac-Toe Game . '''

def board_display(board):
    print("+========" * 3, "+", sep="")
    for i in range(3):
        print("|                 " * 3, "|", sep="")
        for j in range(3):
            print("|       ", str(board[i][j]), "      ", end="")
        print("|")
        print("|                 " * 3, "|", sep="")
        print("+========" * 3, "+", sep="")

board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board_display(board)

def get_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if 1 <= val <= 9:
                return val
            else:
                print("Please enter a valid input from 1-9.")
        except ValueError:
            print("Invalid input. Please enter a number from 1-9.")

def available(board):
    space = []
    players = ["O", "X"]
    for i in range(3):
        for j in range(3):
            if board[i][j] not in players:
                space.append(board[i][j])
    return space

def win(board, player):
    # Check rows, columns, and diagonals
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True
        if board[j][0] == board[j][1] == board[j][2] == player:
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

players = ["O", "X"]
current_player = 0

while True:
    player = players[current_player]
    print(f"Player {player}, make your move.")
    
    val = get_int(": ")
    
    if val not in available(board):
        print("Position already taken. Try again.")
        continue

    for i in range(3):
        for j in range(3):
            if board[i][j] == val:
                board[i][j] = player
                board_display(board)
                break
    
    if win(board, player):
        print(f"Winner is player {player}!")
        break
    
    if not available(board):
        print("The game is a draw!")
        break

    current_player = 1 - current_player
