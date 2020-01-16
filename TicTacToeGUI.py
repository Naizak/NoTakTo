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


# What happens when any of the game board buttons are clicked
def when_clicked(index):
    buttons[index].config(text=current_player, state="disabled", font=("Helvetica", 15))
    flip_player()
    current_player_display = "Player " + current_player + "'s Turn"
    player_label = Label(player_label_frame, text=current_player_display, font=("Helvetica", 15))
    player_label.grid(row=0, column=1)
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
    update_score()


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
        return button0['text']
    elif row_2:
        return button1['text']
    elif row_3:
        return button2['text']
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
        return button0['text']
    elif col_2:
        return button3['text']
    elif col_3:
        return button6['text']
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
        return button0['text']
    elif diagonal_2:
        return button2['text']
    return


# Check if the game has no winner and there are no more spaces on the board to fill
def check_if_tie():
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

    if '' != button0['text'] and button1['text'] and button2['text'] and button3['text'] and button4['text'] and \
            button5['text'] and button6['text'] and button7['text'] and button8['text']:
        game_still_going = False
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Game is a tie.")
    return


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
            player_o_label = Label(game_score_frame, text="Player O's score is: " + str(owins), font=("Helvetica", 15))
            player_o_label.grid(row=2, column=1)
        else:
            tie_games = tie_games+1
            tie_game_label = Label(game_score_frame, text="Draw: " + str(tie_games), font=("Helvetica", 15))
            tie_game_label.grid(row=3, column=1)


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
                    command=lambda index=index: when_clicked(index))
    button.grid(row=r, column=c)
    buttons.append(button)


# Main Loop
root.mainloop()
