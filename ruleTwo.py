from rowColumn import RowColumn


class RuleTwo:

    def __init__(self):
        print("Initializing RuleTwo...")

    def executeRule(self, c, size, isNextOccupied):
        print("executing rule two.....")
        if (0 == c.getRow()) and ((size // 2) == c.getColumn()):
            print("Rule Two succeeds - current r/c:" + str(c.getRow()) + "/" + str(c.getColumn()) + " next r/c:" + str(
                (size - 1)) + "/" + str(c.getColumn() + 1))

            return RowColumn(size - 1, c.getColumn() + 1)
        else:
            print("Rule Two fails - current r/c: " + str(c.getRow()) + "/" + str(c.getColumn()))
            return RowColumn(-3, -3);
