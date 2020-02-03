# Minimax A&D
"""
computer's turn
    keep track of best score
    set best score default to -inf
    check game board for available spots
        FOR IF spot is available
                THEN AI go there
                THEN call minimax (on the board, with a starting depth of 0, and the first move is not the maximizing player) to get score
                THEN undo the move (reset empty string)
                THEN IF score is greater than best score
                        THEN best score becomes the new score
                        THEN best move is this particular position (i, j)
    apply that best move as the computers move


minimax score look up table {X: 1, O: -1, tie: 0}

minimax algorithm (takes in the game board, and the depth)
    check to see if somebody won
    IF somebody won or tied
        THEN the score of the look up table is based on whoever won
        return the score
    IF it is the maximizing player's turn
        THEN set best score to -inf
        THEN check game board for available spots
        FOR IF spot is available
                THEN AI go there
                THEN call minimax (on the board, with a depth + 1, and the first move is not the maximizing player) to get score
                THEN undo the move (reset empty string)
                THEN find the max value between score and best score max(score, best score) set it to best score
    return the best score
    ELSE IF it is the minimizing player's turn
            THEN set best score to +inf
        THEN check game board for available spots
        FOR IF spot is available
                THEN HUMAN go there
                THEN call minimax (on the board, with a depth + 1, and the first move is the maximizing player) to get score
                THEN undo the move (reset empty string)
                THEN find the min value between score and best score min(score, best score) set it to best score
    return the best score
"""

from tkinter import *
import tkinter.messagebox


root = Tk()

# --- Global Variables ---

# If game is still going
game_still_going = True

# Game results
winner = None
xwins = 0
owins = 0
tie_games = 0

# Who's turn is it
current_player = "X"

# minimax score table
scores = {'X': 1, 'O': -1, 'Draw': 0}
# -------------------------


# What happens when any of the game board buttons are clicked
def when_clicked(idx):
    buttons[idx].config(text=current_player, state="disabled", font=("Helvetica", 15))
    flip_player()
    check_if_game_over()


# Swaps between the two players
def flip_player():
    global current_player

    # if current player was x then change it to o
    if current_player == "X":
        current_player = "O"
    # if current player was o then change it to x
    elif current_player == "O":
        current_player = "X"
    return


# Check if the game should end
def check_if_game_over():
    global game_still_going

    check_for_winner()
    if game_still_going:
        check_if_tie()
        if current_player == "O":
            computers_turn()
    update_score()


# MINIMAX potential game states
def check_future_moves():
    global game_still_going

    minimax_check_for_winner()
    if game_still_going:
        minimax_check_if_tie()


# Check if a player has won
def check_for_winner():
    global winner

    row_winner = check_rows()
    col_winner = check_col()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player " + winner + " wins!")
    elif col_winner:
        winner = col_winner
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player " + winner + " wins!")
    elif diagonal_winner:
        winner = diagonal_winner
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player " + winner + " wins!")
    else:
        winner = None

    if row_winner or col_winner or diagonal_winner:

        for i in range(9):
            buttons[i].config(state="disabled")

    return


# MINIMAX potential game states
def minimax_check_for_winner():
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


# Check if play has won by getting three in a row
def check_rows():
    global game_still_going

    # check if any of the rows have the same value and is not empty
    row_1 = buttons[0]['text'] == buttons[3]['text'] == buttons[6]['text'] != ''
    row_2 = buttons[1]['text'] == buttons[4]['text'] == buttons[7]['text'] != ''
    row_3 = buttons[2]['text'] == buttons[5]['text'] == buttons[8]['text'] != ''

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return buttons[0]['text']
    elif row_2:
        return buttons[1]['text']
    elif row_3:
        return buttons[2]['text']
    return


# Check if play has won by getting three in a column
def check_col():
    global game_still_going

    # check if any of the col have the same value and is not empty
    col_1 = buttons[0]['text'] == buttons[1]['text'] == buttons[2]['text'] != ''
    col_2 = buttons[3]['text'] == buttons[4]['text'] == buttons[5]['text'] != ''
    col_3 = buttons[6]['text'] == buttons[7]['text'] == buttons[8]['text'] != ''

    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return buttons[0]['text']
    elif col_2:
        return buttons[3]['text']
    elif col_3:
        return buttons[6]['text']
    return


# Check if play has won by getting three in a diagonal
def check_diagonals():
    global game_still_going

    # check if any of the diagonals have the same value and is not empty
    diagonal_1 = buttons[0]['text'] == buttons[4]['text'] == buttons[8]['text'] != ''
    diagonal_2 = buttons[2]['text'] == buttons[4]['text'] == buttons[6]['text'] != ''

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return buttons[0]['text']
    elif diagonal_2:
        return buttons[2]['text']
    return


# Check if the game has no winner and there are no more spaces on the board to fill
def check_if_tie():
    global game_still_going

    if '' != buttons[0]['text'] and buttons[1]['text'] and buttons[2]['text'] and buttons[3]['text'] \
            and buttons[4]['text'] and buttons[5]['text'] and buttons[6]['text'] and buttons[7]['text'] \
            and buttons[8]['text']:
        game_still_going = False
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Game is a tie.")
    return


# MINIMAX Check if the game has no winner and there are no more spaces on the board to fill
def minimax_check_if_tie():
    global game_still_going

    if '' != buttons[0]['text'] and buttons[1]['text'] and buttons[2]['text'] and buttons[3]['text'] \
            and buttons[4]['text'] and buttons[5]['text'] and buttons[6]['text'] and buttons[7]['text'] \
            and buttons[8]['text']:
        game_still_going = False


# Computers turn, uses minimax
def computers_turn():
    # For Debugging purposes
    """
        best_score = float('inf')
        move = 0
        available_moves = []

        # clear the game board for debugging
        for i in range(9):
            buttons[i].config(text='', state="normal")

        # Hard coded game board
        buttons[0].config(text='X')
        buttons[1].config(text='X')
        buttons[6].config(text='O')
        buttons[7].config(text='O')

        for i in range(9):
            if buttons[i]['text'] == '':
                available_moves.append(i)
        for option in available_moves:
            # If I go to a given option
            buttons[option].config(text='O')
            # what would the score be
            score = minimax(0, True)
            buttons[option].config(text='')
            if score < best_score:
                best_score = score
                move = option

        buttons[move].config(text=current_player, state="disabled", font=("Helvetica", 15))
        flip_player()
        check_if_game_over()
    """

    best_score = float('inf')
    move = 0
    available_moves = []
    for i in range(9):
        if buttons[i]['text'] == '':
            available_moves.append(i)
    for option in available_moves:
        # If I move here
        buttons[option].config(text='O')
        # Then what will the outcome of the game be
        score = minimax(0, float('-inf'), float('inf'), True)
        # Reset the position to blank
        buttons[option].config(text='')
        if score < best_score:
            best_score = score
            move = option

    buttons[move].config(text=current_player, state="disabled", font=("Helvetica", 15))
    flip_player()
    check_if_game_over()


def minimax(depth, alpha, beta, is_maximizing):
    global game_still_going, winner, scores

    check_future_moves()

    if not game_still_going:
        if winner is None:
            winner = "Draw"
        score = scores[winner]
        winner = None
        game_still_going = True
        return score  # DEBUG - Step Into My Code goes to minimax_check_for_winner() but Step Into goes to correct spot
    if is_maximizing:
        best_score = float('-inf')

        for i in range(9):
            if buttons[i]['text'] == '':
                buttons[i].config(text='X')
                check_future_moves()
                score = minimax(depth+1, alpha, beta, False)
                buttons[i].config(text='')
                best_score = max(score, best_score)
                alpha = max(score, alpha)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if buttons[i]['text'] == '':
                buttons[i].config(text='O')
                check_future_moves()
                score = minimax(depth+1, alpha, beta, True)
                buttons[i].config(text='')
                best_score = min(score, best_score)
                beta = min(score, beta)
                if beta <= alpha:
                    break
        return best_score


# Update the score of the game
def update_score():
    global game_still_going, winner, xwins, owins, tie_games

    if not game_still_going:
        if winner == 'X':
            xwins = xwins+1
            player_x_label = Label(game_score_frame, text="Player X's score is: " + str(xwins), font=("Helvetica", 15))
            player_x_label.grid(row=1, column=1)
        elif winner == 'O':
            owins = owins+1
            # WORK AROUND  NOT ACTUAL FIX
            # had to change str(owins) to str(int(owins/2)) because for some reason when O wins the if not gets called
            # twice
            player_o_label = Label(game_score_frame, text="Player O's score is: " + str(int(owins/2)), font=("Helvetica"
                                                                                                             , 15))
            player_o_label.grid(row=2, column=1)
        else:
            tie_games = tie_games+1
            # WORK AROUND  NOT ACTUAL FIX
            # had to change str(tie_games) to str(int(tie_games/2)) because for some reason when ties the if not gets
            # called twice
            tie_game_label = Label(game_score_frame, text="Draw: " + str(int(tie_games/2)), font=("Helvetica", 15))
            tie_game_label.grid(row=3, column=1)


# Restart's the game
def restart_game():
    global game_still_going, current_player

    for i in range(9):
        buttons[i].config(text='', state="normal")

    # Prevents bug of saying the game is tied from the 2nd game and on
    game_still_going = True
    # Makes it so that human is always X and computer is always O
    current_player = "X"


# Making main window and title
root.title("Tic-Tac-Toe")
root.minsize(width=100, height=100)
root.geometry('800x875')

# Making a Menu and Sub Menus
menu = Menu(root)
root.config(menu=menu)

sub_menu = Menu(menu)
menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="New Game", command=restart_game)
sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=quit)

info_menu = Menu(menu)
menu.add_cascade(label="Info", menu=info_menu)
info_menu.add_command(label="About")


# Making frames
player_label_frame = LabelFrame(root)
player_label_frame.pack()
game_board_frame = LabelFrame(root)
game_board_frame.pack()
game_score_frame = LabelFrame(root, text="Score Board")
game_score_frame.pack()


# A list to hold the references to the buttons created below
buttons = []

# Making buttons
for index in range(9):
    r = (index % 3)
    c = int(index/3)

    button = Button(game_board_frame, padx=100, pady=100, width=1, height=1, relief=SUNKEN,
                    command=lambda idx=index: when_clicked(idx))
    button.grid(row=r, column=c)
    buttons.append(button)


# Main Loop
root.mainloop()



