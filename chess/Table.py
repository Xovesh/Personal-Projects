class Table:
    def __init__(self, white, black):
        self.__whitepieces = white
        self.__blackpieces = black
        self.__whitedeadpieces = []
        self.__blackdeadpieces = []
        self.__playboard = self.initialice()

    def initialice(self):
        playb = []
        for i in range(0, 8):
            playb.append([])
            for j in range(0, 8):
                playb[i].append(self.checkpiece(j, i))
        return playb

    def checkpiece(self, x, y):
        for i in self.getpieces():
            if i.getx() == x and i.gety() == y:
                return i
        return None

    def updatepiece(self, piece, x, y):
        self.getplayboard()[piece.gety()][piece.getx()] = None
        self.getplayboard()[y][x] = piece
        piece.setx(x)
        piece.sety(y)

    def deletepiece(self, x, y):
        self.getplayboard()[y][x] = None

    def visualize(self):
        xpositions = ("A", "B", "C", "D", "E", "F", "G", "H")
        print("\nBlack | White eaten Pieces: ", self.getwhitedeadpieces(), "\n")
        for i in range(7, -1, -1):
            print(i+1, end=" ")
            for j in range(0, 8):
                if self.getplayboard()[i][j] is not None:
                    print(self.getplayboard()[i][j], end=" ")
                else:
                    print(" ", end=" ")
            print("")
        print(" ", end=" ")
        for i in xpositions:
            print(i, end=" ")
        print("")
        print("\nWhite | Black eaten Pieces: ", self.getblackdeadpieces())

    def getwhitedeadpieces(self):
        return self.__whitedeadpieces

    def getblackdeadpieces(self):
        return self.__blackdeadpieces

    def getplayboard(self):
        return self.__playboard

    def getwhitepieces(self):
        return self.__whitepieces

    def getblackpieces(self):
        return self.__blackpieces

    def getpieces(self):
        return self.__whitepieces + self.__blackpieces

    def getdeadpieces(self):
        return self.__blackdeadpieces + self.__whitedeadpieces
