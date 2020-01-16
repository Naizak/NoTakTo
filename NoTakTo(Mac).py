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


# What happens when any of the game board buttons are clicked
def when_clicked(index):
    buttons[index].config(text="X", state="disabled", disabledforeground=current_player, font=("Helvetica", 15, "bold"))
    flip_player()
    current_player_display = "Player " + current_player.capitalize() + "'s Turn"
    player_label = Label(player_label_frame, text=current_player_display, font=("Helvetica", 15))
    player_label.grid(row=0, column=1)
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
    update_score()


# Check if a player has won
def check_for_loser():
    global loser
    row_loser = check_rows()
    col_loser = check_col()
    diagonal_loser = check_diagonals()

    if row_loser:
        loser = row_loser
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player " + str(loser).capitalize() + " loses!")
    elif col_loser:
        loser = col_loser
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player " + str(loser).capitalize() + " loses!")
    elif diagonal_loser:
        loser = diagonal_loser
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player " + str(loser).capitalize() + " loses!")
    else:
        loser = None

    if row_loser or col_loser or diagonal_loser:
        button0 = buttons[0]
        button1 = buttons[1]
        button2 = buttons[2]
        button3 = buttons[3]
        button4 = buttons[4]
        button5 = buttons[5]
        button6 = buttons[6]
        button7 = buttons[7]
        button8 = buttons[8]

        button0.config(state="disabled")
        button1.config(state="disabled")
        button2.config(state="disabled")
        button3.config(state="disabled")
        button4.config(state="disabled")
        button5.config(state="disabled")
        button6.config(state="disabled")
        button7.config(state="disabled")
        button8.config(state="disabled")

    return


# Check if play has won by getting three in a row
def check_rows():
    global game_still_going

    button0 = buttons[0]
    button1 = buttons[1]
    button2 = buttons[2]
    button3 = buttons[3]
    button4 = buttons[4]
    button5 = buttons[5]
    button6 = buttons[6]
    button7 = buttons[7]
    button8 = buttons[8]

    # check if any of the rows have the same value and is not empty
    row_1 = button0['text'] == button3['text'] == button6['text'] != ''
    row_2 = button1['text'] == button4['text'] == button7['text'] != ''
    row_3 = button2['text'] == button5['text'] == button8['text'] != ''

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return button0['disabledforeground']
    elif row_2:
        return button1['disabledforeground']
    elif row_3:
        return button2['disabledforeground']
    return


# Check if play has won by getting three in a column
def check_col():
    global game_still_going

    button0 = buttons[0]
    button1 = buttons[1]
    button2 = buttons[2]
    button3 = buttons[3]
    button4 = buttons[4]
    button5 = buttons[5]
    button6 = buttons[6]
    button7 = buttons[7]
    button8 = buttons[8]

    # check if any of the col have the same value and is not empty
    col_1 = button0['text'] == button1['text'] == button2['text'] != ''
    col_2 = button3['text'] == button4['text'] == button5['text'] != ''
    col_3 = button6['text'] == button7['text'] == button8['text'] != ''

    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return button0['disabledforeground']
    elif col_2:
        return button3['disabledforeground']
    elif col_3:
        return button6['disabledforeground']
    return


# Check if play has won by getting three in a diagonal
def check_diagonals():
    global game_still_going

    button0 = buttons[0]
    button2 = buttons[2]
    button4 = buttons[4]
    button6 = buttons[6]
    button8 = buttons[8]

    # check if any of the diagonals have the same value and is not empty
    diagonal_1 = button0['text'] == button4['text'] == button8['text'] != ''
    diagonal_2 = button2['text'] == button4['text'] == button6['text'] != ''

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return button0['disabledforeground']
    elif diagonal_2:
        return button2['disabledforeground']
    return


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
            player_red_label = Label(game_score_frame, text="Player Red's score is: " + str(player_red_wins),
                                     font=("Helvetica", 15))
            player_red_label.grid(row=2, column=1)


# Restart's the game
def restart_game():
    global game_still_going

    button0 = buttons[0]
    button1 = buttons[1]
    button2 = buttons[2]
    button3 = buttons[3]
    button4 = buttons[4]
    button5 = buttons[5]
    button6 = buttons[6]
    button7 = buttons[7]
    button8 = buttons[8]

    button0.config(text='', state="normal")
    button1.config(text='', state="normal")
    button2.config(text='', state="normal")
    button3.config(text='', state="normal")
    button4.config(text='', state="normal")
    button5.config(text='', state="normal")
    button6.config(text='', state="normal")
    button7.config(text='', state="normal")
    button8.config(text='', state="normal")

    # Prevents bug of saying the game is tied from the 2nd game and on
    game_still_going = True


# Making main window and title
root.title("No-Tak-To")
root.minsize(width=100, height=100)
root.geometry('500x500')

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

    button = Button(game_board_frame, padx=50, pady=50, width=1, height=1, relief=SUNKEN, bg='#FDFDE3',
                    command=lambda index=index: when_clicked(index))
    button.grid(row=r, column=c)
    buttons.append(button)


# Main Loop
root.mainloop()
