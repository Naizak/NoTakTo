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
loser = None
player_red_wins = 0
player_blue_wins = 0

# Who's turn is it
current_player = "red"

# Minimax score table
scores = {"red": -1, "blue": 1}

# -------------------------


# What happens when any of the game board buttons are clicked
def when_clicked(idx):
    buttons[idx].config(text='X', state="disabled", disabledforeground=current_player, font=("Helvetica", 15, "bold"))
    flip_player()
    check_if_game_over()


# Swaps between the two players
def flip_player():
    global current_player

    # if current player was red then change it to blue
    if current_player == "red":
        current_player = "blue"
    # if current player was blue then change it to red
    elif current_player == "blue":
        current_player = "red"
    return


# Check if the game should end
def check_if_game_over():
    global game_still_going

    if game_still_going:
        check_for_loser()
    if game_still_going:
        if current_player == "blue":
            computers_turn()
    update_score()


# MINIMAX potential game states
# added an optional attribute in order to keep track of which player was the most recent
def check_future_moves(*args):
    global current_player
    for arg in args:
        if arg == "red":
            current_player = "red"
        elif arg == "blue":
            current_player = "blue"
        else:
            break
    minimax_check_for_loser()


# Check if a player has won
def check_for_loser():
    global game_still_going, loser

    losing_list = []

    # check if any of the rows have the same value and is not empty
    losing_list.append(buttons[0]['text'] == buttons[3]['text'] == buttons[6]['text'] != '')
    losing_list.append(buttons[1]['text'] == buttons[4]['text'] == buttons[7]['text'] != '')
    losing_list.append(buttons[2]['text'] == buttons[5]['text'] == buttons[8]['text'] != '')

    # check if any of the col have the same value and is not empty
    losing_list.append(buttons[0]['text'] == buttons[1]['text'] == buttons[2]['text'] != '')
    losing_list.append(buttons[3]['text'] == buttons[4]['text'] == buttons[5]['text'] != '')
    losing_list.append(buttons[6]['text'] == buttons[7]['text'] == buttons[8]['text'] != '')

    # check if any of the diagonals have the same value and is not empty
    losing_list.append(buttons[0]['text'] == buttons[4]['text'] == buttons[8]['text'] != '')
    losing_list.append(buttons[2]['text'] == buttons[4]['text'] == buttons[6]['text'] != '')

    if any(losing_list):
        game_still_going = False
        flip_player()

        loser = current_player

        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player " + loser.capitalize() + " loses!")
        for i in range(9):
            buttons[i].config(state="disabled")

    return


# MINIMAX potential game states
def minimax_check_for_loser():
    global game_still_going, loser

    losing_list = []

    # check if any of the rows have the same value and is not empty
    losing_list.append(buttons[0]['text'] == buttons[3]['text'] == buttons[6]['text'] != '')
    losing_list.append(buttons[1]['text'] == buttons[4]['text'] == buttons[7]['text'] != '')
    losing_list.append(buttons[2]['text'] == buttons[5]['text'] == buttons[8]['text'] != '')

    # check if any of the col have the same value and is not empty
    losing_list.append(buttons[0]['text'] == buttons[1]['text'] == buttons[2]['text'] != '')
    losing_list.append(buttons[3]['text'] == buttons[4]['text'] == buttons[5]['text'] != '')
    losing_list.append(buttons[6]['text'] == buttons[7]['text'] == buttons[8]['text'] != '')

    # check if any of the diagonals have the same value and is not empty
    losing_list.append(buttons[0]['text'] == buttons[4]['text'] == buttons[8]['text'] != '')
    losing_list.append(buttons[2]['text'] == buttons[4]['text'] == buttons[6]['text'] != '')

    if any(losing_list):
        game_still_going = False
        loser = current_player

    return


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
            buttons[0].config(text='X', state="disabled", disabledforeground=current_player)
            buttons[1].config(text='X', state="disabled", disabledforeground=current_player)
            buttons[6].config(text='X', state="disabled", disabledforeground=current_player)
            buttons[7].config(text='X', state="disabled", disabledforeground=current_player)

            for i in range(9):
                if buttons[i]['text'] == '':
                    available_moves.append(i)
            for option in available_moves:
                # If I go to a given option
                buttons[option].config(text='X', state="disabled", disabledforeground=current_player)
                # what would the score be
                score = minimax(0, float('-inf'), float('inf'), True)
                buttons[option].config(text='', state="normal")
                if score < best_score:
                    best_score = score
                    move = option

            buttons[move].config(text='X', state="disabled", disabledforeground=current_player,
                                 font=("Helvetica", 15, "bold"))
            flip_player()
            check_if_game_over()
    """

    global current_player
    best_score = float('inf')
    move = 0
    available_moves = []

    for i in range(9):
        if buttons[i]['text'] == '':
            available_moves.append(i)
    for option in available_moves:
        # If I move here
        buttons[option].config(text='X', state="disabled", disabledforeground=current_player)
        # Then what will the outcome of the game be
        current_player = "blue"
        score = minimax(0, float('-inf'), float('inf'), True)
        # Reset the position to blank
        buttons[option].config(text='', state="normal")
        if score < best_score:
            best_score = score
            move = option
    current_player = "blue"
    buttons[move].config(text='X', state="disabled", disabledforeground=current_player, font=("Helvetica", 15, "bold"))
    flip_player()
    check_if_game_over()


def minimax(depth, alpha, beta, is_maximizing):
    global game_still_going, loser, scores

    # "if game_still_going" is an optimization choice because when inside of is_maximizing or is_minimizing this check
    # is already done so there is no need to call the function again
    if game_still_going:
        check_future_moves()
    # cannot combine these if statements since we need to check if game is still going after our initial check of the
    # game state
    if not game_still_going:
        score = scores[loser]
        loser = None
        game_still_going = True
        return score

    if is_maximizing:
        best_score = float('-inf')

        for i in range(9):
            if buttons[i]['text'] == '':
                buttons[i].config(text='X', state="disabled", disabledforeground=current_player)
                check_future_moves("red")
                score = minimax(depth+1, alpha, beta, False)
                buttons[i].config(text='', state="normal")
                best_score = max(score, best_score)
                alpha = max(score, alpha)
                if beta <= alpha:
                    break

        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if buttons[i]['text'] == '':
                buttons[i].config(text='X', state="disabled", disabledforeground=current_player)
                check_future_moves("blue")
                score = minimax(depth+1, alpha, beta, True)
                buttons[i].config(text='', state="normal")
                best_score = min(score, best_score)
                beta = min(score, beta)
                if beta <= alpha:
                    break

        return best_score


# Update the score board of the game
def update_score():
    global game_still_going, loser, player_red_wins, player_blue_wins

    if not game_still_going:
        if loser == "red":
            player_blue_wins = player_blue_wins+1
            player_blue_label = Label(game_score_frame, text="Player Blue's score is: " + str(player_blue_wins),
                                      font=("Helvetica", 15))
            player_blue_label.grid(row=1, column=1)
        elif loser == "blue":
            player_red_wins = player_red_wins+1
            # WORK AROUND  NOT ACTUAL FIX
            # had to change str(player_red_wins) to str(int(player_red_wins/2)) because for some reason when player red
            # wins the if not gets called twice
            player_red_label = Label(game_score_frame, text="Player Red's score is: " + str(int(player_red_wins/2)),
                                     font=("Helvetica", 15))
            player_red_label.grid(row=2, column=1)


# Restart's the game
def restart_game():
    global game_still_going, current_player

    for i in range(9):
        buttons[i].config(text='', state="normal")

    # prevent the bug of the player's turn not displaying correctly
    flip_player()
    # prevent the bug of the player's scores still incrementing while the next game is in progress
    game_still_going = True
    # Makes it so that human is always red and computer is always blue
    current_player = "red"


# Making main window and title
root.title("No-Tak-To")
root.minsize(width=100, height=100)
root.geometry('800x875')

# Making a Menu and Sub Menus
menu = Menu(root)
root.config(menu=menu)

sub_menu = Menu(menu)
menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="New Game", command=restart_game)
sub_menu.add_separator()
# sub_menu.add_command(label="Exit", command=quit)

info_menu = Menu(menu)
menu.add_cascade(label="Info", menu=info_menu)
info_menu.add_command(label="About")

# Making frames
player_label_frame = LabelFrame(root)
player_label_frame.pack()
game_board_frame = LabelFrame(root, bg='#FDFDE3')
game_board_frame.pack()
game_score_frame = LabelFrame(root, text="Score Board")
game_score_frame.pack()

# A list to hold the references to the buttons created below
buttons = []

# Making buttons
for index in range(9):
    r = (index % 3)
    c = int(index/3)

    button = Button(game_board_frame, padx=100, pady=100, width=1, height=1, relief=SUNKEN, bg='#FDFDE3',
                    command=lambda idx=index: when_clicked(idx))
    button.grid(row=r, column=c)
    buttons.append(button)

# Main Loop
root.mainloop()
