from chess import Piece


class Queen(Piece.Piece):

    def __init__(self, identificator, color, x, y):
        super().__init__(identificator, color, x, y)
        self.__name = "Queen"
        self.__firstmove = True

    def getfirstmove(self):
        return self.__firstmove

    def setfirstmove(self):
        self.__firstmove = False

    def getname(self):
        return self.__name

    def __str__(self):
        return "Q"

    def __repr__(self):
        return "Q"
