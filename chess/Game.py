from chess import Table
from chess.pieces import Pawn, Queen, Rook, Knight, King, Bishop
import time


class Chess:

    LETTERCONVERSION = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
    REVERSELETTERCONVERSION = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

    # constructor
    def __init__(self):
        self.classic = ([Rook.Rook(0, "White", 0, 0), Knight.Knight(1, "White", 1, 0), Bishop.Bishop(2, "White", 2, 0),
                         Queen.Queen(3, "White", 3, 0), King.King(4, "White", 4, 0), Bishop.Bishop(5, "White", 5, 0),
                         Knight.Knight(6, "White", 6, 0), Rook.Rook(7, "White", 7, 0), Pawn.Pawn(8, "White", 0, 1),
                         Pawn.Pawn(9, "White", 1, 1), Pawn.Pawn(10, "White", 2, 1), Pawn.Pawn(11, "White", 3, 1),
                         Pawn.Pawn(12, "White", 4, 1), Pawn.Pawn(13, "White", 5, 1), Pawn.Pawn(14, "White", 6, 1),
                         Pawn.Pawn(15, "White", 7, 1)],
                        [Pawn.Pawn(16, "Black", 0, 6), Pawn.Pawn(17, "Black", 1, 6), Pawn.Pawn(18, "Black", 2, 6),
                         Pawn.Pawn(19, "Black", 3, 6), Pawn.Pawn(20, "Black", 4, 6), Pawn.Pawn(21, "Black", 5, 6),
                         Pawn.Pawn(22, "Black", 6, 6), Pawn.Pawn(23, "Black", 7, 6), Rook.Rook(24, "Black", 0, 7),
                         Knight.Knight(25, "Black", 1, 7), Bishop.Bishop(26, "Black", 2, 7), King.King(27, "Black", 4, 7),
                         Queen.Queen(28, "Black", 3, 7), Bishop.Bishop(29, "Black", 5, 7), Knight.Knight(30, "Black", 6, 7),
                         Rook.Rook(31, "Black", 7, 7)])

        self.table = Table.Table(self.classic[0], self.classic[1])
        self.shift = "White"
        self.player1 = ("Player 1", "White")
        self.player2 = ("Player 2", "Black")
        self.winner = None
        self.finish = False
        self.time = None

    # starts the timer
    def starttime(self):
        self.time = time.time()

    # returns the time
    def gettime(self):
        return self.time

    # returns the positions available for a pawn
    def pawnmovement(self, j: Pawn.Pawn):
        playb = self.table.getplayboard()
        pawnmovesxy = {"White": (2, 1), "Black": (-2, -1)}
        pawneat = {"White": ((-1, 1), (1, 1)), "Black": ((-1, -1), (1, -1))}
        possiblemovements = []
        k, l = pawnmovesxy[self.shift]
        f = pawneat[self.shift]
        if 0 <= j.gety() + l <= 7:
            if playb[j.gety() + l][j.getx()] is None:
                possiblemovements.append((j.getx(), j.gety() + l))
                print("Pawn can move from", Chess.LETTERCONVERSION[j.getx()], j.gety(), "to: ",
                      Chess.LETTERCONVERSION[j.getx()], j.gety() + l)
                if j.getfirstmove() and 0 <= j.gety() + k <= 7:
                    if playb[j.gety() + k][j.getx()] is None:
                        possiblemovements.append((j.getx(), j.gety() + k))
                        print("Pawn can move from", Chess.LETTERCONVERSION[j.getx()], j.gety(), "to: ",
                              Chess.LETTERCONVERSION[j.getx()], j.gety() + k)
        for o in f:
            if 0 <= j.gety() + o[1] <= 7 and 0 <= j.getx() + o[0] <= 7:
                if playb[j.gety() + o[1]][j.getx() + o[0]] is not None:
                    if playb[j.gety() + o[1]][j.getx() + o[0]].getcolor() is not self.shift:
                        print("Pawn located in ", Chess.LETTERCONVERSION[j.getx()], j.gety(), " can eat ",
                              Chess.LETTERCONVERSION[j.getx() + o[0]], j.gety() + o[1])
                        possiblemovements.append((j.getx() + o[0], j.gety() + o[1]))

        return possiblemovements

    # returns the positions available for a Bishop
    def bishopmovement(self, j: Bishop.Bishop):
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
                                print("%s located in" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                                      " can eat ", Chess.LETTERCONVERSION[j.getx() + l], j.gety() + l)
                            bishopstatus[k] = True
                            break
                if steps > 0:
                    print("%s can move from" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                          "to: ", Chess.LETTERCONVERSION[j.getx() + steps], j.gety() + steps, " maximum")

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
                                print("%s located in" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                                      " can eat ", Chess.LETTERCONVERSION[j.getx() - l], j.gety() + l)
                            bishopstatus[k] = True
                            break
                if steps > 0:
                    print("%s can move from" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                          "to: ", Chess.LETTERCONVERSION[j.getx() - steps], j.gety() + steps, " maximum")

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
                                print("%s located in" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                                      " can eat ", Chess.LETTERCONVERSION[j.getx() - l], j.gety() - l)
                            bishopstatus[k] = True
                            break
                if steps > 0:
                    print("%s can move from" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                          "to: ", Chess.LETTERCONVERSION[j.getx() - steps], j.gety() - steps, " maximum")

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
                                print("%s located in" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                                      " can eat ", Chess.LETTERCONVERSION[j.getx() + l], j.gety() - l)
                            bishopstatus[k] = True
                            break
                if steps > 0:
                    print("%s can move from" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                          "to: ", Chess.LETTERCONVERSION[j.getx() + steps], j.gety() - steps, " maximum")
        return possiblemovements

    # returns the positions available for a rook
    def rookmovement(self, j: Rook.Rook):
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
                                print("%s located in" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                                      " can eat: ", Chess.LETTERCONVERSION[j.getx()], j.gety() - l)
                            rookstatus[k] = True
                            break
                if steps > 0:
                    print("%s can move from" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                          "to: ", Chess.LETTERCONVERSION[j.getx()], j.gety() - steps, " maximum")
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
                                print("%s located in" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                                      " can eat: ", Chess.LETTERCONVERSION[j.getx()], j.gety() + l)
                            rookstatus[k] = True
                            break
                if steps > 0:
                    print("%s can move from" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                          "to: ", Chess.LETTERCONVERSION[j.getx()], j.gety() + steps, " maximum")
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
                                print("%s located in" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                                      " can eat: ", Chess.LETTERCONVERSION[j.getx() - l], j.gety())
                            rookstatus[k] = True
                            break
                if steps > 0:
                    print("%s located in" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                          "to: ", Chess.LETTERCONVERSION[j.getx() - steps], j.gety(), " maximum")
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
                                print("%s located in" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                                      " can eat: ",
                                      Chess.LETTERCONVERSION[j.getx() + l], j.gety())
                            rookstatus[k] = True
                            break
                if steps > 0:
                    print("%s can move from" % j.getname(), Chess.LETTERCONVERSION[j.getx()], j.gety(),
                          "to: ", Chess.LETTERCONVERSION[j.getx() + steps], j.gety(), " maximum")
        return possiblemovements

    # returns the positions available for a king
    def kingmovement(self, j):
        playb = self.table.getplayboard()
        possiblemovements = []
        kingmovesxy = ((-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1))
        for k, l in kingmovesxy:
            if 0 <= j.gety() + l <= 7 and 0 <= j.getx() + k <= 7:
                if playb[j.gety() + l][j.getx() + k] is None:
                    possiblemovements.append((j.getx() + k, j.gety() + l))
                    print("King can move from", Chess.LETTERCONVERSION[j.getx()], j.gety(), "to: ",
                          Chess.LETTERCONVERSION[j.getx() + k], j.gety() + l)
                else:
                    if playb[j.gety() + l][j.getx() + k].getcolor() != self.shift:
                        possiblemovements.append((j.getx() + k, j.gety() + l))
                        print("King located in ", Chess.LETTERCONVERSION[j.getx()], j.gety(), " can eat: ",
                              Chess.LETTERCONVERSION[j.getx() + k], j.gety() + l)
        return possiblemovements

    # returns the positions available for a queen
    def queenmovement(self, j):
        return self.rookmovement(j) + self.bishopmovement(j)

    # returns the positions available for a knight
    def knightmovement(self, j):
        playb = self.table.getplayboard()
        knightmovesxy = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        possiblemovements = []
        for k, l in knightmovesxy:
            if 0 <= j.gety() + l <= 7 and 0 <= j.getx() + k <= 7:
                if playb[j.gety() + l][j.getx() + k] is None:
                    possiblemovements.append((j.getx() + k, j.gety() + l))
                    print("Knight can move from", Chess.LETTERCONVERSION[j.getx()], j.gety(), "to: ",
                          Chess.LETTERCONVERSION[j.getx() + k], j.gety() + l)
                else:
                    if playb[j.gety() + l][j.getx() + k].getcolor() != self.shift:
                        possiblemovements.append((j.getx() + k, j.gety() + l))
                        print("Knight located in", Chess.LETTERCONVERSION[j.getx()], j.gety(), " can eat: ",
                              Chess.LETTERCONVERSION[j.getx() + k], j.gety() + l)
        return possiblemovements

    # moves a piece in xy position
    def movepiece(self, piece, x, y):
        delete = False
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

    # returns if the pawn has reached the final
    @staticmethod
    def pawnfinal(piece):
        if (piece.gety() == 7 or piece.gety() == 0) and piece.getname() == "Pawn":
            return True
        else:
            return False

    # if there can be castling it changes the king and tower postions
    def castling(self, piece):
        if piece.getname() == "Rook" and piece.getfirstmove():
            if self.shift == "White":
                info = self.table.getwhitepieces()
            else:
                info = self.table.getblackpieces()
            king = None
            for i in info:
                if i.getname() == "King":
                    king = i
            if piece.getx() == king.getx() - 1 and king.getfirstmove():
                if self.table.getplayboard()[king.gety()][king.getx() - 2] is None:
                    self.table.updatepiece(king, king.getx() - 2, king.gety())
                    king.setfirstmove()
            elif piece.getx() == king.getx() + 1 and king.getfirstmove():
                if self.table.getplayboard()[king.gety()][king.getx() + 2] is None:
                    self.table.updatepiece(king, king.getx() + 2, king.gety())
                    king.setfirstmove()

    # returns the possible movements of a piece
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

    # transform a piece into another
    def promotioned(self, piece, l):
        position = None
        if piece.getcolor() == "White":
            info = self.table.getwhitepieces()
        else:
            info = self.table.getblackpieces()
        for i in range(0, len(info)):
            if info[i].getid() == piece.getid():
                position = i
                break
        if l == "Bishop":
            k = info[position] = Bishop.Bishop(piece.getid(), piece.getcolor(), piece.getx(), piece.gety())
            self.table.updatepiece(info[position], info[position].getx(), info[position].gety())
        elif l == "Rook":
            k = info[position] = Rook.Rook(piece.getid(), piece.getcolor(), piece.getx(), piece.gety())
            self.table.updatepiece(info[position], info[position].getx(), info[position].gety())
        elif l == "Queen":
            k = info[position] = Queen.Queen(piece.getid(), piece.getcolor(), piece.getx(), piece.gety())
            self.table.updatepiece(info[position], info[position].getx(), info[position].gety())
        elif l == "Knight":
            k = info[position] = Knight.Knight(piece.getid(), piece.getcolor(), piece.getx(), piece.gety())
            self.table.updatepiece(info[position], info[position].getx(), info[position].gety())
        else:
            return None
        return k

    # checks if the king has been eaten
    def checkwinner(self):
        for i in self.table.getwhitedeadpieces():
            if i.getname() == "King":
                self.finish = True
                self.winner = self.player2
        for i in self.table.getblackdeadpieces():
            if i.getname() == "King":
                self.finish = True
                self.winner = self.player1

    # change the shift color
    def changecolor(self):
        self.shift = "Black" if self.shift is "White" else "White"
