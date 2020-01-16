from tkinter import *

Label(None, text='label', fg='green', bg='black').pack()
Button(None, text='button', fg='blue', state="disabled", bg='black').pack()

mainloop()

"""
# keep button from resizing when text appeared in it

from tkinter import *
from itertools import cycle

root = Tk()
root.title("Tic-Tac-Toe")
root.minsize(width=100, height=100)
root.geometry('800x875')

test_frame = Frame(root)
test_frame.grid(row=0, column=0)

fonts = cycle((('Helvetica', '11'), ('Helvetica', '15'), ('Helvetica', '20')))


def chg():
    button.config(font=next(fonts))


# relief=SUNKEN width=40 height=20
button = Button(root, text="Click Me!", padx=100, pady=100, width=1, height=1, command=chg)
button.grid(row=0, column=0)

root.mainloop()
"""

"""
# static size of window
from tkinter import *
root = Tk()
menu = Menu(root)
root.config(menu=menu)

# try fiddling with these root.geometry values
root.title('My tkinter size experiment')
root.minsize(width=100, height=100)
root.geometry('1000x920+0+0')

subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New")
subMenu.add_command(label="Open File...")
subMenu.add_command(label="Close")
subMenu.add_separator()
subMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")

editMenu = Menu(menu)
menu.add_cascade(label="?",menu=editMenu)
editMenu.add_command(label="Check For Updates")
editMenu.add_command(label="Change log")
editMenu.add_command(label="About")


root.mainloop()
"""

"""
# Disabling buttons once clicked edited for TicTacToe
from tkinter import Tk, Button, GROOVE
from itertools import cycle

root = Tk()
current_player = "X"


def when_clicked(index):
    # Disable the button by index
    buttons[index].config(text=current_player, state="disabled")
    flip_player()


def flip_player():
    global current_player
    # if current player was x then change it to o
    if current_player == "X":
        current_player = "O"
    # if current player was o then change it to x
    elif current_player == "O":
        current_player = "X"
    return


# A collection (list) to hold the references to the buttons created below
buttons = []


for index in range(9):

    button = Button(root, bg="White", width=5, height=1, relief=GROOVE, command=lambda index=index: when_clicked(index))

    # Add the button to the window
    button.grid(padx=2, pady=2, row=index % 3, column=int(index / 3))

    # Add a reference to the button to 'buttons'
    buttons.append(button)

root.mainloop()
"""

"""
# Disabling buttons once clicked

from tkinter import Tk, Button, GROOVE

root = Tk()


def appear(index, letter):
    # This line would be where you insert the letter in the textbox
    print(letter)

    # Disable the button by index
    buttons[index].config(state="disabled")


letters=["A", "T", "D", "M", "E", "A", "S", "R", "M"]

# A collection (list) to hold the references to the buttons created below
buttons = []

for index in range(9):
    n = letters[index]

    button = Button(root, bg="White", text=n, width=5, height=1, relief=GROOVE,
                    command=lambda index=index, n=n: appear(index, n))

    # Add the button to the window
    button.grid(padx=2, pady=2, row=index % 3, column=index)

    # Add a reference to the button to 'buttons'
    buttons.append(button)

root.mainloop()
"""