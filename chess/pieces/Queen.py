from chess import Piece


class Queen(Piece.Piece):

    # constructor
    def __init__(self, identificator, color, x, y):
        super().__init__(identificator, color, x, y)
        self.__name = "Queen"

    # returns the name of the piece
    def getname(self):
        return self.__name

    def __str__(self):
        return "Q"

    def __repr__(self):
        return "Q"
