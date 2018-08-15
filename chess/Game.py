from chess import Table
from chess.pieces import Pawn, Queen, Rook, Knight, King, Bishop
import time


class Chess:

    def __init__(self):
        self.classic = ([Rook.Rook(0, "White", 0, 0), Knight.Knight(1, "White", 1, 0), Bishop.Bishop(2, "White", 2, 0),
                        Queen.Queen(3, "White", 3, 0), King.King(4, "White", 4, 0), Bishop.Bishop(5, "White", 5, 0),
                        Knight.Knight(6, "White", 6, 0), Rook.Rook(7, "White", 7, 0), Pawn.Pawn(8, "White", 0, 1),
                        Pawn.Pawn(9, "White", 1, 1), Pawn.Pawn(10, "White", 2, 1), Pawn.Pawn(11, "White", 3, 1),
                        Pawn.Pawn(12, "White", 4, 1), Pawn.Pawn(13, "White", 5, 1), Pawn.Pawn(14, "White", 6, 1),
                        Pawn.Pawn(15, "White", 7, 1)], [Pawn.Pawn(16, "Black", 0, 6), Pawn.Pawn(17, "Black", 1, 6),
                        Pawn.Pawn(18, "Black", 2, 6), Pawn.Pawn(19, "Black", 3, 6), Pawn.Pawn(20, "Black", 4, 6),
                        Pawn.Pawn(21, "Black", 5, 6), Pawn.Pawn(22, "Black", 6, 6), Pawn.Pawn(23, "Black", 7, 6),
                        Rook.Rook(24, "Black", 0, 7), Knight.Knight(25, "Black", 1, 7), Bishop.Bishop(26, "Black", 2, 7),
                        King.King(27, "Black", 4, 7), Queen.Queen(28, "Black", 3, 7), Bishop.Bishop(29, "Black", 5, 7),
                        Knight.Knight(30, "Black", 6, 7), Rook.Rook(31, "Black", 7, 7)])

        self.table = Table.Table(self.classic[0], self.classic[1])
        self.shift = "White"
        self.player1 = ("Player 1", "White")
        self.player2 = ("Player 2", "Black")
        self.letterconversion = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
        self.reverseletterconversion = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        self.winner = None
        self.finish = False
        self.time = None

    def starttime(self):
        self.time = time.time()

    def gettime(self):
        return self.time

    def pawnmovement(self, j):
        playb = self.table.getplayboard()
        pawnmovesxy = {"White": (2, 1), "Black": (-2, -1)}
        pawneat = {"White": ((-1, 1), (1, 1)), "Black": ((-1, -1), (1, -1))}
        possiblemovements = []
        k, l = pawnmovesxy[self.shift]
        f = pawneat[self.shift]
        if 0 <= j.gety() + l <= 7:
            if playb[j.gety() + l][j.getx()] is None:
                possiblemovements.append((j.getx(), j.gety() + l))
                print("Pawn can move from", self.letterconversion[j.getx()], j.gety(), "to: ",
                      self.letterconversion[j.getx()], j.gety() + l)
                if j.getfirstmove() and playb[j.gety() + k][j.getx()] is None and 0 <= j.gety() + k <= 7:
                    possiblemovements.append((j.getx(), j.gety() + k))
                    print("Pawn can move from", self.letterconversion[j.getx()], j.gety(), "to: ",
                          self.letterconversion[j.getx()], j.gety() + k)
        for o in f:
            if 0 <= j.gety() + o[1] <= 7 and 0 <= j.getx() + o[0] <= 7:
                if playb[j.gety() + o[1]][j.getx() + o[0]] is not None and playb[j.gety() + o[1]][j.getx() + o[0]].getcolor() is not self.shift:
                    print("Pawn located in ", self.letterconversion[j.getx()], j.gety(), " can eat ",
                          self.letterconversion[j.getx() + o[0]], j.gety() + o[1])
                    possiblemovements.append((j.getx() + o[0], j.gety() + o[1]))

        return possiblemovements

    def bishopmovement(self, j):
        playb = self.table.getplayboard()
        bishopstatus = {0: False, 1: False, 2: False, 3: False}
        possiblemovements = []
        for k in range(0, 4):
            steps = 0
            # NE
            if k == 0:
                for l in range(1, 8):
                    if j.gety() + l <= 7 and j.getx() + l <= 7:
                        if playb[j.gety() + l][j.getx() + l] is None and not bishopstatus[k]:
                            steps += 1
                            possiblemovements.append((j.getx() + l, j.gety() + l))
                        else:
                            if playb[j.gety() + l][j.getx() + l].getcolor() != self.shift:
                                possiblemovements.append((j.getx() + l, j.gety() + l))
                                print("%s located in" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                                      " can eat ", self.letterconversion[j.getx() + l], j.gety() + l)
                            bishopstatus[k] = True
                            break
                if steps > 0:
                    print("%s can move from" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                          "to: ", self.letterconversion[j.getx() + steps], j.gety() + steps, " maximum")

            # NW
            if k == 1:
                for l in range(1, 8):
                    if j.gety() + l <= 7 and j.getx() - l >= 0:
                        if playb[j.gety() + l][j.getx() - l] is None and not bishopstatus[k]:
                            steps += 1
                            possiblemovements.append((j.getx() - l, j.gety() + l))
                        else:
                            if playb[j.gety() + l][j.getx() - l].getcolor() != self.shift:
                                possiblemovements.append((j.getx() - l, j.gety() + l))
                                print("%s located in" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                                      " can eat ", self.letterconversion[j.getx() - l], j.gety() + l)
                            bishopstatus[k] = True
                            break
                if steps > 0:
                    print("%s can move from" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                          "to: ", self.letterconversion[j.getx() - steps], j.gety() + steps, " maximum")

            # SW
            if k == 2:
                for l in range(1, 8):
                    if j.gety() - l >= 0 and j.getx() - l >= 0:
                        if playb[j.gety() - l][j.getx() - l] is None and not bishopstatus[k]:
                            steps += 1
                            possiblemovements.append((j.getx() - l, j.gety() - l))
                        else:
                            if playb[j.gety() - l][j.getx() - l].getcolor() != self.shift:
                                possiblemovements.append((j.getx() - l, j.gety() - l))
                                print("%s located in" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                                      " can eat ", self.letterconversion[j.getx() - l], j.gety() - l)
                            bishopstatus[k] = True
                            break
                if steps > 0:
                    print("%s can move from" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                          "to: ", self.letterconversion[j.getx() - steps], j.gety() - steps, " maximum")

            # SE
            if k == 3:
                for l in range(1, 8):
                    if j.gety() - l >= 0 and j.getx() + l <= 7:
                        if playb[j.gety() - l][j.getx() + l] is None and not bishopstatus[k]:
                            steps += 1
                            possiblemovements.append((j.getx() + l, j.gety() - l))
                        else:
                            if playb[j.gety() - l][j.getx() + l].getcolor() != self.shift:
                                possiblemovements.append((j.getx() + l, j.gety() - l))
                                print("%s located in" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                                      " can eat ", self.letterconversion[j.getx() + l], j.gety() - l)
                            bishopstatus[k] = True
                            break
                if steps > 0:
                    print("%s can move from" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                          "to: ", self.letterconversion[j.getx() + steps], j.gety() - steps, " maximum")
        return possiblemovements

    def rookmovement(self, j):
        playb = self.table.getplayboard()
        rookstatus = {0: False, 1: False, 2: False, 3: False}
        possiblemovements = []
        for k in range(0, 4):
            steps = 0
            # down
            if k == 0:
                for l in range(1, 8):
                    if j.gety() - l >= 0:
                        if playb[j.gety() - l][j.getx()] is None and not rookstatus[k]:
                            steps += 1
                            possiblemovements.append((j.getx(), j.gety() - l))
                        else:
                            if playb[j.gety() - l][j.getx()].getcolor() != self.shift:
                                possiblemovements.append((j.getx(), j.gety() - l))
                                print("%s located in" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                                      " can eat: ", self.letterconversion[j.getx()], j.gety() - l)
                            rookstatus[k] = True
                            break
                if steps > 0:
                    print("%s can move from" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                          "to: ", self.letterconversion[j.getx()], j.gety() - steps, " maximum")
            # forward
            if k == 1:
                for l in range(1, 8):
                    if j.gety() + l <= 7:
                        if playb[j.gety() + l][j.getx()] is None and not rookstatus[k]:
                            steps += 1
                            possiblemovements.append((j.getx(), j.gety() + l))
                        else:
                            if playb[j.gety() + l][j.getx()].getcolor() != self.shift:
                                possiblemovements.append((j.getx(), j.gety() + l))
                                print("%s located in" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                                      " can eat: ", self.letterconversion[j.getx()], j.gety() + l)
                            rookstatus[k] = True
                            break
                if steps > 0:
                    print("%s can move from" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                          "to: ", self.letterconversion[j.getx()], j.gety() + steps, " maximum")
            # left
            if k == 2:
                for l in range(1, 8):
                    if j.getx() - l >= 0:
                        if playb[j.gety()][j.getx() - l] is None and not rookstatus[k]:
                            steps += 1
                            possiblemovements.append((j.getx() - l, j.gety()))
                        else:
                            if playb[j.gety()][j.getx() - l].getcolor() != self.shift:
                                possiblemovements.append((j.getx() - l, j.gety()))
                                print("%s located in" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                                      " can eat: ", self.letterconversion[j.getx() - l], j.gety())
                            rookstatus[k] = True
                            break
                if steps > 0:
                    print("%s located in" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                          "to: ", self.letterconversion[j.getx() - steps], j.gety(), " maximum")
            # right
            if k == 3:
                for l in range(1, 8):
                    if j.getx() + l <= 7:
                        if playb[j.gety()][j.getx() + l] is None and not rookstatus[k]:
                            steps += 1
                            possiblemovements.append((j.getx() + l, j.gety()))
                        else:
                            if playb[j.gety()][j.getx() + l].getcolor() != self.shift:
                                possiblemovements.append((j.getx() + l, j.gety()))
                                print("%s located in" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                                      " can eat: ",
                                      self.letterconversion[j.getx() + l], j.gety())
                            rookstatus[k] = True
                            break
                if steps > 0:
                    print("%s can move from" % j.getname(), self.letterconversion[j.getx()], j.gety(),
                          "to: ", self.letterconversion[j.getx() + steps], j.gety(), " maximum")
        return possiblemovements

    def kingmovement(self, j):
        playb = self.table.getplayboard()
        possiblemovements = []
        kingmovesxy = ((-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1))
        for k, l in kingmovesxy:
            if 0 <= j.gety() + l <= 7 and 0 <= j.getx() + k <= 7:
                if playb[j.gety() + l][j.getx() + k] is None:
                    possiblemovements.append((j.getx() + k, j.gety() + l))
                    print("King can move from", self.letterconversion[j.getx()], j.gety(), "to: ",
                          self.letterconversion[j.getx() + k], j.gety() + l)
                else:
                    if playb[j.gety() + l][j.getx() + k].getcolor() != self.shift:
                        possiblemovements.append((j.getx() + k, j.gety() + l))
                        print("King located in ", self.letterconversion[j.getx()], j.gety(), " can eat: ",
                              self.letterconversion[j.getx() + k], j.gety() + l)
        return possiblemovements

    def queenmovement(self, j):
        l = self.rookmovement(j)
        k = self.bishopmovement(j)
        return l + k

    def knightmovement(self, j):
        playb = self.table.getplayboard()
        knightmovesxy = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        possiblemovements = []
        for k, l in knightmovesxy:
            if 0 <= j.gety() + l <= 7 and 0 <= j.getx() + k <= 7:
                if playb[j.gety() + l][j.getx() + k] is None:
                    possiblemovements.append((j.getx() + k, j.gety() + l))
                    print("Knight can move from", self.letterconversion[j.getx()], j.gety(), "to: ",
                          self.letterconversion[j.getx() + k], j.gety() + l)
                else:
                    if playb[j.gety() + l][j.getx() + k].getcolor() != self.shift:
                        possiblemovements.append((j.getx() + k, j.gety() + l))
                        print("Knight located in", self.letterconversion[j.getx()], j.gety(), " can eat: ",
                              self.letterconversion[j.getx() + k], j.gety() + l)
        return possiblemovements

    def movepiece(self, piece, x, y):
        delete = False
        try:
            if self.table.getplayboard()[y][x] is not None:
                delete = True
                if piece.getcolor() == "White":
                    info = self.table.getblackpieces()
                    self.table.getblackdeadpieces().append(self.table.getplayboard()[y][x])
                else:
                    info = self.table.getwhitepieces()
                    self.table.getwhitedeadpieces().append(self.table.getplayboard()[y][x])
                for i in range(0, len(info)):
                    if info[i].getid() == self.table.getplayboard()[y][x].getid():
                        info.pop(i)
                        break
            self.table.updatepiece(piece, x, y)
            return delete
        except:
            print("ERROR")

    def pawnfinal(self, piece):
        if (piece.gety() == 7 or piece.gety() == 0) and piece.getname() == "Pawn":
            return True
        else:
            return False

    def checkmovements(self, j):
        if j.getname() is "Knight":
            return self.knightmovement(j)
        elif j.getname() is "Pawn":
            return self.pawnmovement(j)
        elif j.getname() is "Queen":
            return self.queenmovement(j)
        elif j.getname() is "King":
            return self.kingmovement(j)
        elif j.getname() is "Bishop":
            return self.bishopmovement(j)
        elif j.getname() is "Rook":
            return self.rookmovement(j)

    def checkwinner(self):
        for i in self.table.getwhitedeadpieces():
            if i.getname() == "King":
                self.finish = True
                self.winner = self.player2
        for i in self.table.getblackdeadpieces():
            if i.getname() == "King":
                self.finish = True
                self.winner = self.player1

    def changecolor(self):
        if self.shift is "White":
            self.shift = "Black"
        else:
            self.shift = "White"

    # special function to make automatic movements
    def automatico(self):
        #  lista = (
        #     ((4, 2), (4, 4)),
        #     ((4, 7), (4, 5)),
        #     ((5, 2), (5, 4)),
        #     ((4, 5), (5, 4)),
        #     ((6, 1), (5, 3)),
        #     ((6, 7), (6, 5)),
        #     ((5, 1), (2, 4)),
        #     ((6, 5), (6, 4)),
        #     ((3, 2), (3, 4)),
        #     ((6, 4), (5, 3)),
        #     ((3, 1), (5, 3)),
        #     ((5, 8), (7, 6)),
        # )
        # lista2 = (
        #     ((0, 2), (0, 4)),
        #     ((6, 8), (5, 6)),
        #     ((0, 4), (0, 5)),
        #     ((5, 6), (6, 4)),
        #     ((0, 5), (0, 6)),
        #     ((6, 4), (7, 2)),
        #     ((0, 6), (1, 7)),
        #     ((7, 2), (5, 1)),
        #     ((1, 7), (2, 8)),
        #     ((5, 1), (3, 2)),
        # )
        lista3 = (
            ((0, 7), (0, 5)),
            ((6, 1), (5, 3)),
            ((0, 5), (0, 4)),
            ((5, 3), (6, 5)),
            ((0, 4), (0, 3)),
            ((6, 5), (7, 7)),
            ((0, 3), (1, 2)),
            ((7, 7), (5, 8)),
            ((1, 2), (2, 1)),
            ((5, 8), (3, 7)),
        )
        # A=0 B=1 C=2 D=3 E=4 F=5 G=6 H=7
        # piece = None
        # piecename = ""
        for x, y in lista3:
            self.checkmovements()
            # self.table.visualize()
            piece = self.table.getplayboard()[x[1]-1][x[0]]
            piecename = self.table.getplayboard()[x[1]-1][x[0]].getname()
            self.movepiece(piece, y[0], y[1]-1)
            if piecename == "Pawn":
                piece.setfirstmove()
            self.pawnfinal(piece)
            if self.shift is "White":
                self.shift = "Black"
            else:
                self.shift = "White"
        self.table.visualize()
        print("")
        print("Checking info")
        print("")
        print(self.table.getwhitepieces())
        print("")
        print(self.table.getblackpieces())
        print("")
        print(self.table.getplayboard())
        print("")
        print(self.table.getwhitedeadpieces())
        print("")
        print(self.table.getblackdeadpieces())
        print("")
        for i in self.table.getdeadpieces():
            print(i.getname(), i.getx(), i.gety())
