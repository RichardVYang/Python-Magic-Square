from rowColumn import RowColumn


class RuleFive:

    def __init__(self):
        print("Initializing RuleFive...")

    def executeRule(self, c, size, isNextOccupied):
        print("executing rule Five.....")
        if (not isNextOccupied) and (c.getColumn() < size - 1) and (c.getRow() > 0):
            print("Rule Five succeeds - current r/c:" + str(c.getRow()) + "/" + str(c.getColumn()) + " next r/c:" + str(
                (c.getRow() - 1)) + "/" + str(c.getColumn() + 1))
            return RowColumn(c.getRow() - 1, c.getColumn() + 1)
        else:
            print("Rule Five fails - current r/c: " + str(c.getRow()) + "/" + str(c.getColumn()))
            return RowColumn(-3, -3)
