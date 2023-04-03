from rowColumn import RowColumn


class RuleFour:

    def __init__(self):
        print("Initializing RuleFour...")

    def executeRule(self, c, size, isNextOccupied):
        print("executing rule Four.....")
        if ((c.getRow() - 1) >= 0) and ((c.getColumn() == (size - 1))):
            print("Rule Four succeeds - current r/c:" + str(c.getRow()) + "/" + str(c.getColumn()) + " next r/c:" + str(
                (c.getRow() - 1)) + "/" + str((size - size)))
            return RowColumn(c.getRow() - 1, size - size)
        else:
            print("Rule Four fails - current r/c: " + str(c.getRow()) + "/" + str(c.getColumn()))
            return RowColumn(-3, -3)
