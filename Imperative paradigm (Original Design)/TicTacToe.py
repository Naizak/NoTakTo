# board
# display board
# play game
# handel turn
# check win
    # check rows
    # check col
    # check diagonals
# check tie
    # if board is full and no win
# flip player

# ---- Global Variables ----

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_still_going = True

# Game results
winner = None

# Who's turn is it
current_player = "x"


def display_board():
    print(board[6] + " | " + board[7] + " | " + board[8])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[0] + " | " + board[1] + " | " + board[2])


def play_game():
    # Display initial board
    display_board()
    # While the game is still going
    while game_still_going:
        # handle a single turn of an arbitrary player
        handle_turn(current_player)
        # Check if the game has ended
        check_if_game_over()
        # Flip to the other player
        flip_player()
    # The game has ended
    if winner == "x" or winner == "o":
        print(winner + " won.")
    elif winner is None:
        print("Tie.")


# Handle a single turn of an arbitrary player
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Position already taken. Go again.")

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner
    row_winner = check_rows()
    col_winner = check_col()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


def check_rows():
    global game_still_going
    # check if any of the rows have the same value and is not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_col():
    global game_still_going
    # check if any of the col have the same value and is not empty
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonals():
    global game_still_going
    # check if any of the diagonals have the same value and is not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player
    # if current player was x then change it to o
    if current_player == "x":
        current_player = "o"
    # if current player was o then change it to x
    elif current_player == "o":
        current_player = "x"
    return


play_game()