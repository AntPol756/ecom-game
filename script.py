

if __name__ == '__main__':
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    current_player = "O"
    winner = " "
    game_running = True

#printing the game board
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#take player input
def player_input(board):
    inp =  int(input(f"Please enter a number between 1 and 9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = current_player
    else:
        print(f"This spot is already taken, please try another spot.")

#check for win or tie
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("it's a tie!")
        game_running = False

#switch the player

#check for win or tie again

while game_running:
    print_board(board)
    player_input(board)
    check_horizontal(board)
    check_row(board)
    check_diagonal(board)
    check_tie(board)
