
class Piece:
    def __init__(self, identificator, color, x, y):
        self.__id = identificator
        self.__color = color
        self.__x = x
        self.__y = y

    def getid(self):
        return self.__id

    def getcolor(self):
        return self.__color

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def setx(self, x):
        self.__x = x

    def sety(self, y):
        self.__y = y
