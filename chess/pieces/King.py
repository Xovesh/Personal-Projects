from chess import Piece


class King(Piece.Piece):

    def __init__(self, identificator, color, x, y):
        super().__init__(identificator, color, x, y)
        self.__name = "King"
        self.__check = False

    def getname(self):
        return self.__name

    def __str__(self):
        return "K"

    def __repr__(self):
        return "K"
