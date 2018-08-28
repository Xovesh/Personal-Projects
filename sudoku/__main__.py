from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
import time
from sudoku import Game


class App:

    # constructor
    def __init__(self):
        self.sudoku = None
        self.numbers = []
        self.canvasgrid = []
        self.root = Tk()
        self.root.geometry("930x757")
        self.root.resizable(0, 0)
        self.root.title("Sudoku")
        self.game = Frame(self.root)
        self.right = Frame(self.root)
        self.table()
        self.timer = None
        mainloop()

    def table(self):
        for i in range(0, 9):
            self.canvasgrid.append([])
            for j in range(0, 9):
                self.canvasgrid[i].append(Canvas(self.game, width=80, height=80, highlightbackground="black"))
                self.canvasgrid[i][-1].grid(row=i, column=j)
        self.game.grid(row=0, column=0)

        self.startbutton = Button(self.right, text="Start", command=self.start, width=20, height=4)
        self.startbutton.grid(row=0, column=0)

        self.time = Label(self.right, text="Time: 0s")
        self.time.grid(row=1, column=0, pady=10)

        self.checkbutton = Button(self.right, text="Check Sudoku", state=DISABLED, width=20, height=4)
        self.checkbutton.grid(row=2, column=0, pady=10)

        self.right.grid(row=0, column=1, sticky=N, padx=10)

    def start(self):
        self.startbutton.config(state=DISABLED, text="The game Started!")
        self.checkbutton.config(state=ACTIVE, command=self.checksudoku)
        self.sudoku = Game.SudokuGame()
        self.starttime()
        self.visualizenumbers()
        while not self.sudoku.getfinish():
            self.updatetimelabel()
            self.root.update()
        self.root.destroy()

    def starttime(self):
        self.timer = time.time()

    def updatetimelabel(self):
        self.time.config(text="Time: " + str(int(time.time()-self.timer)) + "s")

    def checksudoku(self):
        if self.sudoku.checkall():
            messagebox.showinfo("Sudoku Game", "The Sudoku is correct!!! Thanks for playing")
            self.sudoku.setfinish()
        else:
            messagebox.showinfo("Sudoku Game", "There are some errors, please check them")
            for i in self.sudoku.wrongpositions():
                self.canvasgrid[i[1]][i[0]].config(bg="red")

    def changenumber(self, sv, x, y):
        try:
            if 1 <= int(sv.get()) <= 9:
                self.sudoku.table.setxy(x, y, int(sv.get()))
                self.canvasgrid[y][x].config(bg="#f0f0f0")
            else:
                sv.set("")
                self.sudoku.table.setxy(x, y, 0)
        except:
            sv.set("")

        self.sudoku.table.visualize()

    # visualizes the numbers in the table
    def visualizenumbers(self):
        font1 = Font(family="Times New Roman", size=20)
        for i in range(0, 9):
            self.numbers.append([])
            for j in range(0, 9):
                if self.sudoku.table.getxy(i, j) != 0:
                    self.numbers[i].append(ttk.Label(self.game, text=self.sudoku.table.getxy(i, j), font=font1))
                else:
                    sv = StringVar()
                    sv.trace_add("write", lambda name, index, mode, sv=sv, x=i, y=j: self.changenumber(sv, x, y))
                    self.numbers[i].append(Entry(self.game, width=1, font=font1, textvariable=sv))

                self.numbers[i][-1].grid(row=j, column=i)


a = App()
