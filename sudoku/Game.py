from sudoku import Sudoku
import random

class SudokuGame:
    def __init__(self):
        self.table = Sudoku.Sudoku()
        self.initialize()

    def initialize(self):
        for i in range(0, 30):
            while True:
                number = random.randint(1, 9)
                numberx = random.randint(0, 8)
                numbery = random.randint(0, 8)
                if self.table.getxy(numberx, numbery) == 0:
                    self.table.setxy(numberx, numbery, number)
                    while not self.checkxy(numberx, numbery):
                        number = random.randint(1, 9)
                        self.table.setxy(numberx, numbery, number)
                    break
        self.table.visualize()

    def checkxy(self, x, y):
        # check column
        for i in range(0, 9):
            if self.table.getxy(x, i) == self.table.getxy(x, y) and y != i:
                return False

        # check row
        for j in range(0, 9):
            if self.table.getxy(j, y) == self.table.getxy(x, y) and x != j:
                return False

        # check square
        square = self.table.getsquare(x, y)
        for i in range(square[0][0], square[0][1]+1):
            for j in range(square[1][0], square[1][1]+1):
                if self.table.getxy(x, y) == self.table.getxy(i, j) and x != i and y != j:
                    return False
        return True

    def checkall(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if not self.checkxy(i, j):
                    print("There are some errors")
                    return False
        return True

#
# a = SudokuGame()
#
# while True:
#     x = int(input("X value: "))
#     y = int(input("Y value: "))
#     n = int(input("Number value: "))
#     a.table.setxy(x, y, n)
#     a.table.visualize()
