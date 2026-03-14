

if __name__ == '__main__':
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    current_player = "x"
    winner = " "
    game_running = True

#printing the game board
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
print_board(board)
#take player input

#check for win or tie

#switch the player

#check for win or tie again
