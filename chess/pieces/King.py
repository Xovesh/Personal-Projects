from chess import Piece


class King(Piece.Piece):

    # constructor
    def __init__(self, identificator, color, x, y):
        super().__init__(identificator, color, x, y)
        self.__name = "King"
        self.__check = False

    # returns the check condition
    def getcheck(self):
        return self.__check

    # set check parameter to the condition given True/False
    def setcheck(self, condition: bool):
        self.__check = condition

    # returns the name of the piece
    def getname(self):
        return self.__name

    def __str__(self):
        return "K"

    def __repr__(self):
        return "K"
