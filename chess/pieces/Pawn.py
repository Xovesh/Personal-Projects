from chess import Piece


class Pawn(Piece.Piece):

    def __init__(self, identificator, color, x, y):
        super().__init__(identificator, color, x, y)
        self.__name = "Pawn"
        self.__firstmove = True

    def getname(self):
        return self.__name

    def getfirstmove(self):
        return self.__firstmove

    def setfirstmove(self):
        self.__firstmove = False

    def __str__(self):
        return "P"

    def __repr__(self):
        return "P"
