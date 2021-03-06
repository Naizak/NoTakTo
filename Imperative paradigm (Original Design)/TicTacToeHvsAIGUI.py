from tkinter import *
import tkinter.messagebox
import random

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

"""

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

"""


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


# Computers turn, picks at random
def computers_turn():
    global game_still_going
    if game_still_going:
        available_moves = []
        for i in range(9):
            if buttons[i]['text'] == '':
                available_moves.append(i)
        computers_choice = random.choice(available_moves) # minimax will replace this step
        buttons[computers_choice].config(text=current_player, state="disabled", font=("Helvetica", 15))
        flip_player()
        check_if_game_over()


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
            # had to change str(owins) to str(int(owins/2)) because for some reason when O wins the if not gets called
            # twice
            player_o_label = Label(game_score_frame, text="Player O's score is: " + str(int(owins/2)), font=("Helvetica"
                                                                                                             , 15))
            player_o_label.grid(row=2, column=1)
        else:
            tie_games = tie_games+1
            tie_game_label = Label(game_score_frame, text="Draw: " + str(tie_games), font=("Helvetica", 15))
            tie_game_label.grid(row=3, column=1)


# Restart's the game
def restart_game():
    global game_still_going, current_player

    for i in range(9):
        buttons[i].config(text='', state="normal")

    # Prevents bug of saying the game is tied from the 2nd game and on
    game_still_going = True
    # Makes it so that human is always X and computer is always O
    current_player = 'X'


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
