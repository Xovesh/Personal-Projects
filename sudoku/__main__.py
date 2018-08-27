from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
import time
from PIL import ImageTk, Image
from sudoku import Game


class App:

    # constructor
    def __init__(self):
        self.sudoku = None
        self.numbers = []
        self.root = Tk()
        self.root.geometry("930x757")
        self.root.resizable(0, 0)
        self.root.title("Sudoku")
        self.game = Frame(self.root)
        self.right = Frame(self.root)
        self.table()
        mainloop()

    def table(self):
        for i in range(0, 9):
            for j in range(0, 9):
                Canvas(self.game, width=80, height=80, highlightbackground="black").grid(row=i, column=j)
        self.game.grid(row=0, column=0)

        self.startbutton = Button(self.right, text="Start", command=self.start, width=20, height=4)
        self.startbutton.grid(row=0, column=0)
        self.right.grid(row=0, column=1, sticky=N, padx=10)

    def start(self):
        self.startbutton.config(state=DISABLED, text="The game Started!")
        self.sudoku = Game.SudokuGame()
        self.visualizenumbers()
        while True:
            self.root.update()

    # visualizes the pieces in the table
    def visualizenumbers(self):
        font1 = Font(family="Times New Roman", size=20)
        for i in range(0, 9):
            for j in range(0, 9):
                if self.sudoku.table.getxy(i, j) != 0:
                    self.numbers.append(ttk.Label(self.game, text=self.sudoku.table.getxy(i, j), font=font1))
                else:
                    self.numbers.append(Entry(self.game, width=1, font=font1))
                self.numbers[-1].grid(row=j, column=i)



a = App()
