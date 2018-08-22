from chess import Game
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
import time
from PIL import ImageTk, Image


# icons by Freepik


class App:
    IMAGESWHITE = {"Pawn": "Icons/WhitePawn.png", "Rook": "Icons/WhiteRook.png",
                   "Bishop": "Icons/WhiteBishop.png", "King": "Icons/WhiteKing.png",
                   "Knight": "Icons/WhiteKnight.png", "Queen": "Icons/WhiteQueen.png"}

    IMAGESBLACK = {"Pawn": "Icons/BlackPawn.png", "Rook": "Icons/BlackRook.png",
                   "Bishop": "Icons/BlackBishop.png", "King": "Icons/BlackKing.png",
                   "Knight": "Icons/BlackKnight.png", "Queen": "Icons/BlackQueen.png"}

    # constructor
    def __init__(self):
        self.chess = Game.Chess()
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.geometry("920x740")
        self.root.iconbitmap('icon.ico')
        self.root.resizable(0, 0)
        self.root.title("Classic Chess")

        self.left = Frame(self.root)
        self.bottom = Frame(self.root)
        self.right = Frame(self.root)
        self.game = Frame(self.root)
        self.lastmovements = []
        self.piecesposition = {}

        self.table()
        mainloop()

    # starts the game
    def start(self):
        self.startbutton.config(state=DISABLED, text="The game Started!")
        self.pieces()
        self.visualizepieces()
        self.chess.starttime()
        shift = "White"
        while not self.chess.finish:
            while self.chess.shift == shift:
                self.time()
                self.root.update()
            if shift == "White":
                shift = "Black"
            else:
                shift = "White"
            self.chess.checkwinner()
            self.visualizepieces()
        messagebox.showinfo("Classic Chess", "Game Finished, the winner is " + self.chess.winner[0])
        self.root.destroy()

    # time update
    def time(self):
        self.label3.config(text="Time: " + str(int(time.time() - self.chess.gettime())) + "s")

    # give to each piece a button
    def pieces(self):
        for j in self.chess.table.getpieces():
            if j.getcolor() == "White":
                img = ImageTk.PhotoImage(Image.open(App.IMAGESWHITE[j.getname()]).convert("RGBA"))
            else:
                img = ImageTk.PhotoImage(Image.open(App.IMAGESBLACK[j.getname()]).convert("RGBA"))
            self.piecesposition[j.getid()] = Button(self.game, text=j.getname() + "\n" + j.getcolor(), relief=FLAT,
                                                    command=lambda piece=j: self.movements(piece), image=img, bg="#E6E6E6")
            self.piecesposition[j.getid()].image = img

    # creates the buttons to move
    def movements(self, piece):
        self.clearmovements()
        self.lastmovements.clear()
        for i in self.chess.checkmovements(piece):
            self.lastmovements.append(Button(self.game, text="Move Here", command=lambda x=i[0], y=i[1]: self.move(piece, x, y), relief=FLAT))
            self.lastmovements[-1].grid(row=9 - i[1] - 2, column=i[0])

    # destroys the buttons
    def clearmovements(self):
        for l in self.lastmovements:
            l.destroy()

    # checks executed when moving a piece
    def checks(self, piece):
        if self.chess.pawnfinal(piece):
            self.promotion(piece)
        self.chess.castling(piece)
        piece.setfirstmove()

    # piece eaten
    def delete(self):
        if self.chess.shift == "White":
            k = (self.chess.table.getwhitedeadpieces(), self.deadwhite)
        else:
            k = (self.chess.table.getblackdeadpieces(), self.deadblack)
        j = len(k[0])
        if j > 12:
            l = 3
            j = j - 12
        elif j > 8:
            l = 2
            j = j - 8
        elif j > 4:
            l = 1
            j = j - 4
        else:
            l = 0
        self.piecesposition[k[0][-1].getid()].destroy()
        self.piecesposition[k[0][-1].getid()] = Button(k[1], text=k[0][-1].getname(), state=DISABLED).grid(row=l, column=j)

    # move a piece
    def move(self, piece, x, y):
        s = self.chess.movepiece(piece, x, y)
        self.clearmovements()
        self.checks(piece)
        self.chess.changecolor()
        if s:
            self.delete()
        self.chess.table.visualize()

    # you cant close the promotion window
    def noclosing(self):
        pass

    # Close main window
    def close(self):
        messagebox.showinfo("Classic Chess", "Thanks for Playing")
        self.root.destroy()

    # pawn promotion window
    def promotion(self, piece):
        self.top = Toplevel(self.root, height=100, width=100)
        self.root.protocol("WM_DELETE_WINDOW", self.noclosing)
        self.top.protocol("WM_DELETE_WINDOW", self.noclosing)
        Label(self.top, text="Pawn promotion ", width=20, height=4).grid(row=0, column=1)
        Label(self.top, text="Select One", width=20, height=4).grid(row=0, column=2)
        Button(self.top, text="Bishop", command=lambda l="Bishop": self.proselect(piece, l), width=20, height=4).grid(row=1, column=0)
        Button(self.top, text="Rook", command=lambda l="Rook": self.proselect(piece, l), width=20, height=4).grid(row=1, column=1)
        Button(self.top, text="Queen", command=lambda l="Queen": self.proselect(piece, l), width=20, height=4).grid(row=1, column=2)
        Button(self.top, text="Knight", command=lambda l="Knight": self.proselect(piece, l), width=20, height=4).grid(row=1, column=3)
        self.visualizepieces(arg="disabled")
        self.root.wait_window(self.top)

    # pawn transformation
    def proselect(self, piece, l):
        j = self.chess.promotioned(piece, l)
        self.piecesposition[piece.getid()].destroy()
        if j.getcolor() == "White":
            img = ImageTk.PhotoImage(Image.open(App.IMAGESWHITE[j.getname()]).convert("RGBA"))
        else:
            img = ImageTk.PhotoImage(Image.open(App.IMAGESBLACK[j.getname()]).convert("RGBA"))
        self.piecesposition[j.getid()] = Button(self.game, text=j.getname() + "\n" + j.getcolor(), relief=FLAT, command=lambda: self.movements(j), image=img, bg="#E6E6E6")
        self.piecesposition[j.getid()].image = img
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.top.destroy()

    # visualizes the pieces in the table
    def visualizepieces(self, arg="normal"):
        for r in self.chess.table.getpieces():
            if self.chess.shift != r.getcolor():
                self.piecesposition[r.getid()].config(state=DISABLED)
            else:
                self.piecesposition[r.getid()].config(state=arg)
            self.piecesposition[r.getid()].grid(row=9 - r.gety() - 2, column=r.getx())

    # creates the canvas for the playground
    def gametable(self):
        for i in range(0, 8):
            if i % 2 == 0:
                colors = ("white", "black")
            else:
                colors = ("black", "white")
            for j in range(0, 8):
                if j % 2 != 0:
                    color = colors[0]
                else:
                    color = colors[1]
                Canvas(self.game, width=80, height=80, bg=color).grid(row=i, column=j)
        self.game.grid(row=0, column=1)

    # creates the full table
    def table(self):
        letters = "ABCDEFGH"
        font1 = Font(family="Times New Roman", size=20)
        font2 = Font(family="Times New Roman", size=36)

        for i in range(0, 8):
            j = 9 - i - 1
            label = ttk.Label(self.left, text=str(j))
            label.config(font=font2)
            label.grid(row=i, column=0, ipady=12)
        for i in range(0, len(letters)):
            label = ttk.Label(self.bottom, text=str(letters[i]))
            label.config(font=font2)
            label.grid(row=0, column=i, padx=24)
        self.left.grid(row=0, column=0, sticky=N)
        self.bottom.grid(row=1, column=1)

        self.gametable()

        self.startbutton = Button(self.right, text="Start", command=self.start, width=20, height=4)
        self.startbutton.grid(row=0, column=0)

        self.label3 = ttk.Label(self.right, text="")
        self.label3.grid(row=1, column=0)

        label = ttk.Label(self.right, text="Dead White Pieces", font=font1)
        label.grid(row=2, column=0)

        self.deadwhite = Frame(self.right)
        self.deadwhite.grid(row=3, column=0)

        label2 = ttk.Label(self.right, text="Dead Black Pieces", font=font1)
        label2.grid(row=4, column=0)

        self.deadblack = Frame(self.right)
        self.deadblack.grid(row=5, column=0)

        self.right.grid(row=0, column=2, sticky=(N, S), pady=25)


a = App()
