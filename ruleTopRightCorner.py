from rowColumn import RowColumn


class RuleTopRightCorner:

    def __init__(self):
        print("Initializing RuleTopRightCorner...")

    def executeRule(self, c, size, isNextOccupied):
        print("executing rule TopRightCorner.....")
        if (0 == c.getRow()) and (c.getColumn() == (size - 1)):
            print("Rule TopRightCorner succeeds - current r/c:" + str(c.getRow()) + "/" + str(
                c.getColumn()) + " next r/c:" + str((c.getRow() + 1)) + "/" + str(c.getColumn()))
            return RowColumn(c.getRow() + 1, c.getColumn())
        else:
            print("Rule TopRightCorner fails - current r/c: " + str(c.getRow()) + "/" + str(c.getColumn()))
            return RowColumn(-3, -3)
