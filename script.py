import random

def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

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
                print(f"Out of range! please enter a number between 1 and 9")
        except ValueError:
            print(f"Invalid input Please enter a number between 1 and 9!")

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
        return True
    return False

def check_win(board):
    global game_running
    if check_horizontal(board) or check_row(board) or check_diagonal(board):
        return True
    return False

def play_game():
    global game_running
    global board
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    while True:
        play = input(f"Welcome to Tic-Tac-Toe, to play press y for yes or n for no: ").lower()
        if play == "y":
            break
        elif play == "n":
            print("Goodbye")
            game_running = False
            return
        else:
            print("Invalid input! Please type y for yes or n for no.")


    player1_name = input("Player 1, pleas enter your name: ")
    while True:
        is_computer = input("If you want to play against a Human press 1 or if you want to play against a Computer press 2:")
        if is_computer == "2":
            player2_name = "Computer"
            break
        elif is_computer == "1":
            player2_name = input("Player 2, pleas enter your name: ")
            break
        else:
            print("Invalid choice! Please enter 1 for playing against another player or 2 for playing against a computer.")

    while True:
        choice = input(f"{player1_name}, pick a symbol X or O or press Enter for random: ").upper()
        if choice == 'X' or choice == 'O':
            player1_symbol = choice
            break

        elif choice == "":
            player1_symbol = random.choice(["X", "O"])
            print(f"Randomly assigned: {player1_symbol}")
            break

        else:
            print("Invalid choice! Please type X or O or just press Enter.")

    if player1_symbol == "X":
            player2_symbol = "O"
    else:
        player2_symbol = "X"

    current_turn = player1_symbol
    names = {player1_symbol: player1_name, player2_symbol: player2_name}
    while game_running == True:
        print_board(board)

        if is_computer == "2" and names[current_turn] == "Computer":
            print("The computer is making a move pleas wait")

            available_spots = []
            for i in range(len(board)):
                if board[i] == "-":
                    available_spots.append(i)
            move_index = random.choice(available_spots)
        else:
            move_index = player_input(names[current_turn], board) - 1

        board[move_index] = current_turn

        if check_win(board):
            print_board(board)
            print(f"The winner is {names[current_turn]}!")
            game_running = False

        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            game_running = False

        else:
            if current_turn == "X":
                current_turn = "O"
            else:
                current_turn = "X"

if __name__ == '__main__':
    winner = " "
    while True:
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]

        game_running = True
        play_game()
        play_again = input("Game Over, would you like to play again? (y/n): ").lower()
        if play_again.lower() == "n":
            print("Thanks for playing!  goodbye.")
            break