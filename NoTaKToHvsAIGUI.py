from tkinter import *
import tkinter.messagebox
import random

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

# minimax score table
scores = {'red': 1, 'blue': -1}


# What happens when any of the game board buttons are clicked
def when_clicked(idx):
    buttons[idx].config(text="X", state="disabled", disabledforeground=current_player, font=("Helvetica", 15, "bold"))
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

    check_for_loser()
    if game_still_going:
        if current_player == "blue":
            computers_turn()
    update_score()


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

"""
# minimax_check_winner()
if ai is about to get 3 in a row do not go there
"""


# Computers turn, uses minimax
def computers_turn():

    available_moves = []
    for i in range(9):
        if buttons[i]['text'] == '':
            available_moves.append(i)
    computers_move = random.choice(available_moves)
    buttons[computers_move].config(text="X", state="disabled", disabledforeground=current_player,
                                   font=("Helvetica", 15, "bold"))
    flip_player()
    check_if_game_over()


# Update the score of the game
def update_score():
    global game_still_going, loser, player_red_wins, player_blue_wins

    if not game_still_going:
        if loser == 'red':
            player_blue_wins = player_blue_wins+1
            player_blue_label = Label(game_score_frame, text="Player Blue's score is: " + str(player_blue_wins),
                                      font=("Helvetica", 15))
            player_blue_label.grid(row=1, column=1)
        elif loser == 'blue':
            player_red_wins = player_red_wins+1
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
    # Makes it so that human is always X and computer is always O
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
sub_menu.add_command(label="Exit", command=quit)

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
