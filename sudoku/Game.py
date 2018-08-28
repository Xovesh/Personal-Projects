from sudoku import Sudoku


class SudokuGame:
    SUDOKU1 = [[0, 0, 2, 6, 0, 0, 0, 8, 0],
               [0, 0, 0, 8, 9, 0, 0, 4, 5],
               [0, 8, 0, 3, 4, 0, 0, 6, 0],
               [0, 0, 6, 0, 3, 5, 0, 0, 0],
               [8, 0, 0, 0, 0, 6, 0, 0, 7],
               [5, 4, 0, 0, 0, 0, 0, 0, 0],
               [0, 7, 8, 5, 2, 0, 0, 0, 4],
               [0, 5, 0, 9, 0, 4, 0, 0, 0],
               [6, 0, 0, 0, 7, 8, 0, 2, 0]]

    # for checking purpose

    SUDOKU2 = [[4, 1, 2, 6, 5, 7, 3, 8, 9],
               [3, 6, 7, 8, 9, 2, 1, 4, 5],
               [9, 8, 5, 3, 4, 1, 7, 6, 2],
               [7, 2, 6, 4, 3, 5, 9, 1, 8],
               [8, 3, 9, 2, 1, 6, 4, 5, 7],
               [5, 4, 1, 7, 8, 9, 2, 3, 6],
               [1, 7, 8, 5, 2, 3, 6, 9, 4],
               [2, 5, 3, 9, 6, 4, 8, 7, 1],
               [6, 9, 4, 1, 7, 8, 5, 2, 0]]

    def __init__(self):
        self.table = Sudoku.Sudoku()
        self.finish = False
        self.gamenumbers = []
        self.initialize()
        self.table.visualize()

    def initialize(self):
        self.table.board = SudokuGame.SUDOKU1
        for i in range(0, 9):
            for j in range(0, 9):
                if SudokuGame.SUDOKU1[i][j] == 0:
                    self.gamenumbers.append((j, i))

    def getfinish(self):
        return self.finish

    def setfinish(self):
        self.finish = True

    def checkcolumn(self, x, y):
        for i in range(0, 9):
            if self.table.getxy(x, i) == self.table.getxy(x, y) and y != i:
                return False
        return True

    def checkrow(self, x, y):
        for j in range(0, 9):
            if self.table.getxy(j, y) == self.table.getxy(x, y) and x != j:
                return False
        return True

    def checksquare(self, x, y):
        square = self.table.getsquare(x, y)
        for i in range(square[0][0], square[0][1] + 1):
            for j in range(square[1][0], square[1][1] + 1):
                if self.table.getxy(x, y) == self.table.getxy(i, j) and x != i and y != j:
                    return False
        return True

    def checkxy(self, x, y):
        if self.table.getxy(x, y) != 0:
            if self.checkcolumn(x, y) and self.checkrow(x, y) and self.checksquare(x, y):
                return True
            else:
                return False
        else:
            return False

    def checkall(self):
        for i in self.gamenumbers:
            if not self.checkxy(i[0], i[1]):
                return False
        return True

    def wrongpositions(self):
        positionswrong = []
        for i in self.gamenumbers:
                if not self.checkxy(i[0], i[1]):
                    positionswrong.append((i[0], i[1]))

        return positionswrong
