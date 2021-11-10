# NoTakTo Description

NoTakTo is inspired by Tic-Tac-Toe. 
In Tic-Tac-Toe you and your opponent have your own set of shapes and you are trying to get 3 in a row to win.
In NoTakTo you and your opponent share the same shape and the first one to get 3 in a row loses.
You can play both Tic-Tac-Toe and NoTakTo in this program.
Your opponent is an AI that uses MiniMax and AB pruning to select the most optional move against you.
I would like to implement the NoTakTo portion of this project to have the ability to use multiple game boards. So instead of a typical 3x3 board you could have a 3x9 board instead.

# File Structure

The file structure looks like this:

.idea

Resources

executables

notakto-main

notakto-oop

The ***.idea folder*** is a default folder created by the IDE I used PyCharm.
The ***Resources folder*** contains all of the research I did for the project.
The ***executables folder*** contains .exe demos of both the Tic-Tac-Toe and NoTakTo games that can be tried out.
The ***notakto-main folder*** contains the main files of the project.
The ***notakto-oop folder*** contains the progress being done to try and implement an oop paradigm in order to try and create a gameboard object so that I can create multiple gameboard instances for Notakto.

# Contents of the notakto-main folder

Inside this folder is all of the python scripts created during this project. The design was to start off small and work my way to the finished project. Anything with the word Mac before it was designed to fit the resolution of a 15 inch Macbook Pro screen, as I was working on this program on both my desktop and Macbook at the same time. So in ***order of progression from earliest to latest is***:

TicTacToe.py – 2 human players for Tic-Tac-Toe on the terminal

TicTacToeHvsAI.py – 1 AI and 1 human player for Tic-Tac-Toe on the terminal

Mac-TicTacToeGUI.py – 2 human players for Tic-Tac-Toe on the tkinter GUI using a Macbook

TicTacToeGUI.py – 2 human players for Tic-Tac-Toe on the tkinter GUI

Mac-NoTakToGUI.py – 2 human players for NoTakTo on the tkinter GUI using a Macbook

NoTakToGUI.py – 2 human players for NoTakTo on the tkinter GUI

TicTacToeHvsAIGUI.py – 1 AI and 1 human player for Tic-Tac-Toe on the tkinter GUI

NoTaKToHvsAIGUI.py – 1 AI and 1 human player for NoTakTo on the tkinter GUI

Mac-MiniMax(TicTakToe).py – 1 improved AI and 1 human player for Tic-Tac-Toe on the tkinter GUI using a Macbook

MiniMax(TicTacToe).py – 1 improved AI and 1 human player for Tic-Tac-Toe on the tkinter GUI

Mac-MiniMax(NoTakTo).py – 1 improved AI and 1 human player for NoTakTo on the tkinter GUI using a Macbook

MiniMax(NoTakTo).py – 1 improved AI and 1 human player for NoTakTo on the tkinter GUI

# How to use project

As of now the only way to run the project natively on devices other than Windows would be to run the actual .py files on an IDE. For Windows devices you should be able to run the .exe files in the executable folder
