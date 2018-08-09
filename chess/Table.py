class Table:
    def __init__(self, white, black):
        self.whitepieces = white
        self.blackpieces = black
        self.whitedeadpieces = []
        self.blackdeadpieces = []
        self.playboard = self.initialice()

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
        self.playboard[piece.gety()][piece.getx()] = None
        self.playboard[y][x] = piece
        piece.setx(x)
        piece.sety(y)

    def deletepiece(self, x, y):
        self.playboard[y][x] = None

    def visualize(self):
        xpositions = ("A", "B", "C", "D", "E", "F", "G", "H")
        print("\nBlack | White eaten Pieces: ", self.getwhitedeadpieces(), "\n")
        for i in range(7, -1, -1):
            print(i, end=" ")
            for j in range(0, 8):
                if self.playboard[i][j] is not None:
                    print(self.playboard[i][j], end=" ")
                else:
                    print(" ", end=" ")
            print("")
        print(" ", end=" ")
        for i in xpositions:
            print(i, end=" ")
        print("")
        print("\nWhite | Black eaten Pieces: ", self.getblackdeadpieces())

    def getwhitedeadpieces(self):
        return self.whitedeadpieces

    def getblackdeadpieces(self):
        return self.blackdeadpieces

    def getplayboard(self):
        return self.playboard

    def getwhitepieces(self):
        return self.whitepieces

    def getblackpieces(self):
        return self.blackpieces

    def getpieces(self):
        return self.whitepieces + self.blackpieces