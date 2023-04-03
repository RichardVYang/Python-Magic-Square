# main.py

import magicSquare


def startMain(size):
    print('Main square size:', size)
    magicSquareObj = magicSquare.MagicSquare(size)

    magicSquareObj.start()


# Entry point/main function function of Python
if __name__ == '__main__':
    size = 5  # magic square size must be odd number, ie, 3, 5, 7, 9, 11, 13, etc. There are even Magic Square as well.

    startMain(size)
