
class Piece:

    # constructor
    def __init__(self, identificator, color, x, y):
        self.__id = identificator
        self.__color = color
        self.__x = x
        self.__y = y
        self.__firstmove = True

    # returns the firstmove status
    def getfirstmove(self):
        return self.__firstmove

    # set the firstmove status to false
    def setfirstmove(self):
        self.__firstmove = False

    # returns the piece id
    def getid(self):
        return self.__id

    # returns the piece color
    def getcolor(self):
        return self.__color

    # returns the piece x value
    def getx(self):
        return self.__x

    # returns the piece y value
    def gety(self):
        return self.__y

    # sets the piece with new x
    def setx(self, x):
        self.__x = x

    # sets the piece with new y
    def sety(self, y):
        self.__y = y

    # returns the piece xy value
    def getxy(self):
        return self.__x, self.__y

    # sets the piece with new xy
    def setxy(self, x, y):
        self.__x = x
        self.__y = y
