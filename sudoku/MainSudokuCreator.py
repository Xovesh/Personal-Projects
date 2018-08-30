from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
from sudoku import sudokucreator


class App:

    # constructor
    def __init__(self, debug=False):
        self.debug = debug
        self.matrixnumbers = []
        self.numbers = []
        self.canvasgrid = []
        self.root = Tk()
        self.root.geometry("930x757")
        self.root.resizable(0, 0)
        self.root.title("SudokuCreator")
        self.root.iconbitmap('icon.ico')
        self.game = Frame(self.root)
        self.right = Frame(self.root)
        self.table()
        mainloop()

    def canvas(self):
        for i in range(0, 9):
            self.canvasgrid.append([])
            for j in range(0, 9):
                Canvas(self.game, width=80, height=80, highlightbackground="black").grid(row=i, column=j)
        self.game.grid(row=0, column=0)

    def matrix(self):
        for i in range(0, 9):
            self.matrixnumbers.append([])
            for j in range(0, 9):
                self.matrixnumbers[i].append(0)

    def table(self):
        self.canvas()
        self.matrix()
        savebutton = Button(self.right, text="Save", command=lambda: self.save(), width=20, height=4)
        savebutton.grid(row=0, column=0)
        clearbutton = Button(self.right, text="Clear", command=lambda: self.clear(), width=20, height=4)
        clearbutton.grid(row=1, column=0, pady=10)
        if self.debug:
            debugbutton = Button(self.right, text="Debug", command=lambda: self.visualizematrixnumbers(), width=20, height=4)
            debugbutton.grid(row=3, column=0)
        self.right.grid(row=0, column=1, sticky=N, padx=10, pady=10)
        self.visualizenumbers()

    def save(self):
        sudokucreator.insersudoku(self.matrixnumbers)
        messagebox.showinfo("SudokuCreator", "Sudoku Created Successfully, you can check it in sudokulist.csv file")

    def clear(self):
        for i in range(0, 9):
            for j in range(0, 9):
                self.numbers[i][j].delete(0, END)
                self.numbers[i][j].insert(0, 0)

    def changenumber(self, sv, x, y):
        try:
            if 1 <= int(sv.get()) <= 9:
                self.matrixnumbers[y][x] = int(sv.get())
            else:
                sv.set("")
                self.matrixnumbers[y][x] = 0
        except:
            sv.set("")
            self.matrixnumbers[y][x] = 0

    # visualizes the numbers in the table
    def visualizenumbers(self):
        font1 = Font(family="Times New Roman", size=20)
        for i in range(0, 9):
            self.numbers.append([])
            for j in range(0, 9):
                sv = StringVar()
                sv.trace_add("write", lambda name, index, mode, st=sv, x=i, y=j: self.changenumber(st, x, y))
                self.numbers[i].append(Entry(self.game, width=1, font=font1, textvariable=sv))
                self.numbers[i][-1].grid(row=j, column=i)

    def visualizematrixnumbers(self):
        print("")
        for i in range(0, 9):
            for j in range(0, 9):
                print(self.matrixnumbers[i][j], end=" ")
            print("")


a = App()
