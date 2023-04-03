# magicSquare.py

import rowColumn

import ruleManager

# import rowColumn
from rowColumn import RowColumn


class MagicSquare:

    def __init__(self, mSize):
        self.size = mSize

        self.currentPosition = RowColumn(-1, -1)
        self.newPosition = RowColumn(-1, -1)

        rows, cols = (mSize, mSize)
        self.square = [[0 for i in range(cols)] for j in range(rows)]
        print("Magic Square:  ", self.square)

    def start(self):
        print('Magic square start size:', self.size)

        rulemanagerobject = ruleManager.RuleManager(self.size)
        isNextPositionOccupied = False
        maxNumber = self.size * self.size

        for magicNumber in range(maxNumber):
            newPosition = rulemanagerobject.getNextPosition(self.currentPosition, self.size, isNextPositionOccupied)
            row = newPosition.getRow()
            column = newPosition.getColumn()

            if ((row >= 0) and (column >= 0) and (row <= self.size - 1) and (column <= self.size - 1)):
                #       print("======> Using square[{0}][{1}] = {2}: ".format(row, column,magicNumber ))
                self.square[row][column] = (magicNumber + 1)  # magicNumber starts with 0.
                self.currentPosition = newPosition
                if (row > 0 and column < self.size - 1) and (self.square[row - 1][column + 1] > 0):
                    isNextPositionOccupied = True
                else:
                    isNextPositionOccupied = False
            else:
                print("Encounter invalid row/column number outside the square magic row and column...")

            self.displaySquareInProgress(self.square, self.size)
            print("---------------------------")

        print("************* Below is your official magic square! *****************\n")
        self.displayMagicSquareResult(self.square, self.size)

    def displaySquareInProgress(self, square, size):
        print("displaySquareInProgress")
        txt = " {:>2}"
        for row in range(size):
            for column in range(size):
                print(txt.format(self.square[row][column]), end=" ")

            print()  # print carrier return!

    def displayMagicSquareResult(self, square, size):
        self.displayMagicSquareWithRowSum(self.square, self.size)
        self.displayColumnSum(self.square, self.size)
        self.displayDiagonalSum(self.square, self.size)

    def displayMagicSquareWithRowSum(self, square, size):
        for row in range(size):
            columnSum = 0
            for column in range(size):
                columnSum = columnSum + self.square[row][column]
                txt = " {:>2}"
                print(txt.format(self.square[row][column]), end=" ")

            print("  = ", columnSum)

    def displayColumnSum(self, square, size):
        print("  =========")

        for column in range(size):
            rowSum = 0;
            for row in range(size):
                rowSum = rowSum + self.square[row][column]

            print(" {:>2}".format(rowSum), end=" ")

        print()  # print carrier return for next line

    def displayDiagonalSum(self, square, size):
        leftDiagonalSum = 0
        rightDiagonalSum = 0

        for d in range(size):
            leftDiagonalSum = leftDiagonalSum + self.square[d][d]
            rightDiagonalSum = rightDiagonalSum + self.square[(self.size - 1) - d][d]

        leftDiag = "Sum of left diagonal: {}".format(leftDiagonalSum)
        rightDiag = "Sum of right diagonal: {}".format(rightDiagonalSum)

        print(leftDiag + "  " + rightDiag)
