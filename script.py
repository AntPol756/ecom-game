import random



#printing the game board
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#take player input
def player_input(player_name,board):
    while True:
        try:
            turn = int(input(f"Player {player_name}, Please enter a number between 1 and 9: "))
            if 1 <= turn <=9 :
                if board[turn - 1] == "-":
                    return turn
                else:
                    print(f"This spot is already taken, please try another spot.")
            else:
                print(f"Please enter a number between 1 and 9")
        except ValueError:
            print("Invalid input Please enter a number between 1 and 9!")
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

def check_win():
    global game_running
    if check_horizontal(board) or check_row(board) or check_diagonal(board):
        print(f"The winner is {winner}")
        game_running = False


#switch the player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# computer player
#def computer(board):
 #   while current_player == "O":
  #      position = random.randint(0, 9)
  #      if board[position] == "-":
   #         board[position] = "O"
    #        switch_player()


def play_game():
    global game_running
    while True:
        play = input(f"Welcome to Tic-Tac-Toe, would you like to play? press y for yes or n for no: ")
        if play.lower() == "n":
            print("Thanks for playing!")
            break

# Setup Players
    player1_name = input("Player 1, pleas enter your name: ")
    is_computer = input("Do you want to play against (1) Human or (2) Computer? ")
    if is_computer == "2":
        player2_name = "Computer"
    else:
        player2_name = input("Player 2, pleas enter your name: ")

    choice = input(f"{player1_name}, pick a symbol (X/O) or press Enter for random: ").upper()
    if choice != 'X' and choice != 'O':
            player1_symbol = random.choice(["X", "O"])
            print(f"Randomly assigned: {player1_symbol}")
    else:
            player1_symbol = choice

    if player1_symbol == "X":
            player2_symbol = "O"
    else:
            player2_symbol = "X"


    current_turn = player1_symbol
    names = {player1_symbol: player1_name, player2_symbol: player2_name}
    while game_running:
        print_board(board)

        if is_computer and names[current_turn] == "Computer":
            print("Computer is making a move...")

            available_spots = [i for i, spot in enumerate(board) if spot == "-"]
            move_index = random.choice(available_spots)
        else:
            # Human move
            move_index = player_input(names[current_turn], board) - 1

        board[move_index] = current_turn

        # 4. Check Win/Tie
        if check_horizontal(board) or check_row(board) or check_diagonal(board):
            print_board(board)
            print(f"The winner is {names[current_turn]}!")
            game_running = False
        elif "-" not in board:
            print_board(board)
            print("It's a tie!")
            game_running = False
        else:
            # 5. Switch Player
            current_turn = "O" if current_turn == "X" else "X"

    # 6. Play Again?
        if input("Would you like to play again? (y/n): ").lower() == "y":
            board = ["-", "-", "-",
                     "-", "-", "-",
                     "-", "-", "-"]
            game_running = True
            play_game()

if __name__ == '__main__':
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]


    turn = 0
    winner = " "
    game_running = True
    play_game()
