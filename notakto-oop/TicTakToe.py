from tkinter import *
import tkinter.messagebox


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


# Check if play has won by getting three in a row
def check_rows(buttons):
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
def check_col(buttons):
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
def check_diagonals(buttons):
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

    # Check if a player has won


# Check if a player has won
def check_for_winner(buttons):
    global winner

    row_winner = check_rows(buttons)
    col_winner = check_col(buttons)
    diagonal_winner = check_diagonals(buttons)

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
def minimax_check_for_winner(buttons):
    global winner

    row_winner = check_rows(buttons)
    col_winner = check_col(buttons)
    diagonal_winner = check_diagonals(buttons)

    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


# Check if the game has no winner and there are no more spaces on the board to fill
def check_if_tie(buttons):
    global game_still_going

    if '' != buttons[0]['text'] and buttons[1]['text'] and buttons[2]['text'] and buttons[3]['text'] \
            and buttons[4]['text'] and buttons[5]['text'] and buttons[6]['text'] and buttons[7]['text'] \
            and buttons[8]['text']:
        game_still_going = False
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Game is a tie.")
    return


# MINIMAX Check if the game has no winner and there are no more spaces on the board to fill
def minimax_check_if_tie(buttons):
    global game_still_going

    if '' != buttons[0]['text'] and buttons[1]['text'] and buttons[2]['text'] and buttons[3]['text'] \
            and buttons[4]['text'] and buttons[5]['text'] and buttons[6]['text'] and buttons[7]['text'] \
            and buttons[8]['text']:
        game_still_going = False


# MINIMAX potential game states
def check_future_moves(buttons):
    global game_still_going

    minimax_check_for_winner(buttons)
    if game_still_going:
        minimax_check_if_tie(buttons)


# Restart's the game
def restart_game(buttons):
    global game_still_going, current_player

    for i in range(9):
        if len(buttons) != 0:
            buttons[i].config(text='', state="normal")

    # Prevents bug of saying the game is tied from the 2nd game and on
    game_still_going = True
    # Makes it so that human is always X and computer is always O
    current_player = "X"


class TicTakToeApp(Frame):

    # What happens when any of the game board buttons are clicked
    def when_clicked(self, buttons, idx):
        buttons[idx].config(text=current_player, state="disabled", font=("Helvetica", 15))
        flip_player()
        self.check_if_game_over(buttons)

    # Check if the game should end
    def check_if_game_over(self, buttons):
        global game_still_going

        if game_still_going:
            check_for_winner(buttons)
        if game_still_going:
            check_if_tie(buttons)
            if current_player == "O":
                self.computers_turn(buttons)
        self.update_score()

    # Computers turn, uses minimax
    def computers_turn(self, buttons):

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
            score = self.minimax(buttons, 0, float('-inf'), float('inf'), True)
            # Reset the position to blank
            buttons[option].config(text='')
            if score < best_score:
                best_score = score
                move = option

        buttons[move].config(text=current_player, state="disabled", font=("Helvetica", 15))
        flip_player()
        self.check_if_game_over(buttons)

    def minimax(self, buttons, depth, alpha, beta, is_maximizing):
        global game_still_going, winner, scores

        check_future_moves(buttons)

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
                    check_future_moves(buttons)
                    score = self.minimax(buttons, depth + 1, alpha, beta, False)
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
                    check_future_moves(buttons)
                    score = self.minimax(buttons, depth + 1, alpha, beta, True)
                    buttons[i].config(text='')
                    best_score = min(score, best_score)
                    beta = min(score, beta)
                    if beta <= alpha:
                        break
            return best_score

    # Update the score of the game
    def update_score(self):
        global game_still_going, winner, xwins, owins, tie_games

        if not game_still_going:
            if winner == 'X':
                xwins = xwins + 1
                player_x_label = Label(self.game_score_frame, text="Player X's score is: " + str(xwins),
                                       font=("Helvetica", 15))
                player_x_label.grid(row=1, column=1)
            elif winner == 'O':
                owins = owins + 1
                # WORK AROUND  NOT ACTUAL FIX
                # had to change str(owins) to str(int(owins/2)) because for some reason when O wins the if not gets called
                # twice
                player_o_label = Label(self.game_score_frame, text="Player O's score is: " + str(int(owins / 2)),
                                       font=("Helvetica"
                                             , 15))
                player_o_label.grid(row=2, column=1)
            else:
                tie_games = tie_games + 1
                # WORK AROUND  NOT ACTUAL FIX
                # had to change str(tie_games) to str(int(tie_games/2)) because for some reason when ties the if not gets
                # called twice
                tie_game_label = Label(self.game_score_frame, text="Draw: " + str(int(tie_games / 2)),
                                       font=("Helvetica", 15))
                tie_game_label.grid(row=3, column=1)

    # Constructor creates frames and buttons
    def __init__(self, master=None, buttons=None):

        Frame.__init__(self, master)
        if buttons is None:
            buttons = []
        self.master = master
        self.init_window(buttons)

        # Making frames
        self.player_label_frame = LabelFrame(root)
        self.player_label_frame.pack()
        self.game_board_frame = LabelFrame(root)
        self.game_board_frame.pack()
        self.game_score_frame = LabelFrame(root, text="Score Board")
        self.game_score_frame.pack()

        # Making buttons
        self.create_buttons(master)

    # Creates window
    def init_window(self, buttons):

        # Making main window and title
        self.master.title("Tic-Tac-Toe")
        self.master.minsize(width=100, height=100)
        self.master.geometry('800x875')

        # Making a Menu and Sub Menus
        menu = Menu(self.master)
        self.master.config(menu=menu)

        sub_menu = Menu(menu)
        menu.add_cascade(label="File", menu=sub_menu)
        sub_menu.add_command(label="New Game", command=restart_game(buttons))
        sub_menu.add_separator()
        sub_menu.add_command(label="Exit", command=quit)

        info_menu = Menu(menu)
        menu.add_cascade(label="Info", menu=info_menu)
        info_menu.add_command(label="About")

    # Creates buttons
    def create_buttons(self, master):
        # A list to hold the references to the buttons created below
        buttons = []

        for index in range(9):
            r = (index % 3)
            c = int(index / 3)

            button = Button(self.game_board_frame, padx=100, pady=100, width=1, height=1, relief=SUNKEN,
                            command=lambda idx=index: self.when_clicked(buttons, idx))
            button.grid(row=r, column=c)
            buttons.append(button)

        return buttons


root = Tk()
game = TicTakToeApp(root)
root.mainloop()



