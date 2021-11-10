from tkinter import *


def print_message():
    print("Wow this actually worked!")


# the class creates the window and creates and packs the buttons into the window
class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.print_button = Button(frame, text="Print Message", command=print_message)
        self.print_button.pack(side=LEFT)

        self.quit_button = Button(frame, text="Quit", command=frame.quit)
        self.quit_button.pack(side=LEFT)


root = Tk()
obj = App(root)
root.mainloop()
