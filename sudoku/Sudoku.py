class Sudoku:
    def __init__(self):
        self.board = []
        self.squares = {1: ((0, 2), (0, 2)), 2: ((3, 5), (0, 2)), 3: ((6, 8), (0, 2)),
                        4: ((0, 2), (3, 5)), 5: ((3, 5), (3, 5)), 6: ((6, 8), (3, 5)),
                        7: ((0, 2), (6, 8)), 8: ((3, 5), (6, 8)), 9: ((6, 8), (6, 8))}
        self.initialize()

    def visualize(self):
        print("   0 1 2 3 4 5 6 7 8")
        print(" │¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        for i in range(0, 9):
            print(i, end="│ ")
            for j in range(0, 9):
                if self.board[i][j] == 0:
                    print("_", end=" ")
                else:
                    print(self.board[i][j], end=" ")
            print("")

    def initialize(self):
        for i in range(0, 9):
            self.board.append([])
            for j in range(0, 9):
                self.board[i].append(0)

    def getxy(self, x, y):
        return self.board[y][x]

    def setxy(self, x, y, n):
        self.board[y][x] = n

    def getsquare(self, x, y):
        if 0 <= x <= 2:
            if 0 <= y <= 2:
                return self.squares[1]
            elif 2 <= y <= 5:
                return self.squares[4]
            else:
                return self.squares[7]
        elif 2 <= x <= 5:
            if 0 <= y <= 2:
                return self.squares[2]
            elif 2 <= y <= 5:
                return self.squares[5]
            else:
                return self.squares[8]
        else:
            if 0 <= y <= 2:
                return self.squares[3]
            elif 2 <= y <= 5:
                return self.squares[6]
            else:
                return self.squares[9]

    def deletexy(self, x, y):
        self.setxy(x, y, 0)

    def getboard(self):
        return self.board
