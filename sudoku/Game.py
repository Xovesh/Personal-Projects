from sudoku import Sudoku


class SudokuGame:
    def __init__(self, n):
        self.table = Sudoku.Sudoku()
        self.finish = False
        # available position that can be modified
        self.gamenumbers = []
        self.initialize(n)

    def visualize(self):
        self.table.visualize()

    def initialize(self, n):
        self.table.copy(n)
        for i in range(0, 9):
            for j in range(0, 9):
                if self.table.getboard()[i][j] == 0:
                    self.gamenumbers.append((j, i))

    def getfinish(self):
        return self.finish

    def setfinish(self):
        self.finish = True

    def getgamenumbers(self):
        return self.gamenumbers

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
