class Table:

    # constructor
    def __init__(self, white, black):
        self.__whitepieces = white
        self.__blackpieces = black
        self.__whitedeadpieces = []
        self.__blackdeadpieces = []
        self.__playboard = self.initialice()

    # initialice the playboard | initialice and __checkpiece needs an update for better performance
    def initialice(self):
        playb = []
        for i in range(0, 8):
            playb.append([])
            for j in range(0, 8):
                playb[i].append(self.__checkpiece(j, i))
        return playb

    # returns the piece with the position xy
    def __checkpiece(self, x, y):
        for i in self.getpieces():
            if i.getx() == x and i.gety() == y:
                return i
        return None

    # returns the piece with the ID given
    def getpieceid(self, k):
        for i in self.getdeadandlivepieces():
            if i.getid() == k:
                return i

    # updates the piece position in the new coordinates
    def updatepiece(self, piece, x, y):
        self.getplayboard()[piece.gety()][piece.getx()] = None
        self.getplayboard()[y][x] = piece
        piece.setxy(x, y)

    # deletes the piece in the position given
    def deletepiece(self, x, y):
        self.getplayboard()[y][x] = None

    # visualizes in the console the game Table
    def visualize(self):
        xpositions = "ABCDEFGH"
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

    # returns the white dead pieces
    def getwhitedeadpieces(self):
        return self.__whitedeadpieces

    # returns the black dead pieces
    def getblackdeadpieces(self):
        return self.__blackdeadpieces

    # returns the playboard
    def getplayboard(self):
        return self.__playboard

    # returns the live white pieces
    def getwhitepieces(self):
        return self.__whitepieces

    # returns the live white pieces
    def getblackpieces(self):
        return self.__blackpieces

    # returns the live white and black pieces
    def getpieces(self):
        return self.__whitepieces + self.__blackpieces

    # returns the dead white and black pieces
    def getdeadpieces(self):
        return self.__blackdeadpieces + self.__whitedeadpieces

    # returns the live and dead white and black pieces
    def getdeadandlivepieces(self):
        return self.getpieces() + self.getdeadpieces()
