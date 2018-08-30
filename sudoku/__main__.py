from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
import time
from sudoku import Game, sudokucreator


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
        self.root.iconbitmap('icon.ico')
        self.game = Frame(self.root)
        self.right = Frame(self.root)
        self.table()
        self.timer = None
        mainloop()

    def canvas(self, final=False):
        for i in range(0, 9):
            if final:
                self.canvasgrid.append([])
            for j in range(0, 9):
                if final:
                    self.canvasgrid[i].append(Canvas(self.game, width=80, height=80, highlightbackground="black"))
                    self.canvasgrid[i][-1].grid(row=i, column=j)
                else:
                    Canvas(self.game, width=80, height=80, highlightbackground="black").grid(row=i, column=j)
        self.game.grid(row=0, column=0)

    def table(self):
        self.canvas()

        self.startbutton = Button(self.right, text="Select a Sudoku", state=DISABLED, width=20, height=4)
        self.startbutton.grid(row=0, column=0)

        self.time = Label(self.right, text="Time: 0s")
        self.time.grid(row=1, column=0, pady=10)

        self.checkbutton = Button(self.right, text="Check Sudoku", state=DISABLED, width=20, height=4)
        self.checkbutton.grid(row=2, column=0, pady=10)

        self.randomgeneratorbutton = Button(self.right, text="Generate Random", width=20, height=4)
        self.randomgeneratorbutton.grid(row=4, column=0, pady=10)
        # sudoku list viewer

        self.listsudoku = ttk.Frame(self.right)
        self.scrollbar = Scrollbar(self.listsudoku)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.listbox = Listbox(self.listsudoku, yscrollcommand=self.scrollbar.set)
        for i in range(0, sudokucreator.getlastid() + 1):
            try:
                self.listbox.insert(END, "Sudoku: " + str(i))
            except:
                pass

        self.listbox.bind("<<ListboxSelect>>", self.displaysudoku)
        self.listbox.pack(side=LEFT, fill=BOTH)

        self.scrollbar.config(command=self.listbox.yview)

        self.listsudoku.grid(column=0, row=3, sticky=(N, S, E))

        # end sudoku list viewer
        self.right.grid(row=0, column=1, sticky=N, padx=10)

    def displaysudoku(self, event):
        w = event.widget
        list_item = w.curselection()
        if len(list_item) != 0:
            self.previsualizenumbers(list_item[0])
            self.startbutton.config(text="Start Game", state=NORMAL, command=lambda n=list_item[0]: self.start(n))

    def start(self, n):
        self.listsudoku.grid_remove()
        self.scrollbar.grid_remove()
        self.randomgeneratorbutton.grid_remove()
        self.startbutton.config(state=DISABLED, text="The game Started!")
        self.checkbutton.config(state=ACTIVE, command=self.checksudoku)
        self.sudoku = Game.SudokuGame(sudokucreator.getsudokubyid(n))
        self.starttime()
        self.canvas(final=True)
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
            for i in self.sudoku.getgamenumbers():
                self.canvasgrid[i[1]][i[0]].config(bg="#f0f0f0")
                if not self.sudoku.checkxy(i[0], i[1]):
                    self.canvasgrid[i[1]][i[0]].config(bg="red")

    def changenumber(self, sv, x, y):
        print(sv.get())
        try:
            if 1 <= int(sv.get()) <= 9:
                self.sudoku.table.setxy(x, y, int(sv.get()))
                self.canvasgrid[y][x].config(bg="#f0f0f0")
            else:
                sv.set("")
                self.sudoku.table.setxy(x, y, 0)
        except:
            sv.set("")
            self.sudoku.table.setxy(x, y, 0)
            
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
                    sv.trace_add("write", lambda name, index, mode, st=sv, x=i, y=j: self.changenumber(st, x, y))
                    self.numbers[i].append(Entry(self.game, width=1, font=font1, textvariable=sv))

                self.numbers[i][-1].grid(row=j, column=i)

    # previsualization of the numbers
    def previsualizenumbers(self, n):
        self.canvas()
        font1 = Font(family="Times New Roman", size=20)
        sudoku = sudokucreator.getsudokubyid(n)
        for i in range(0, 9):
            for j in range(0, 9):
                if sudoku[i][j] != 0:
                    ttk.Label(self.game, text=sudoku[i][j], font=font1).grid(row=i, column=j)
                else:
                    ttk.Label(self.game, font=font1).grid(row=i, column=j)


a = App()
