from rowColumn import RowColumn


class RuleEight:

    def __init__(self):
        print("Initializing RuleEight...")

    def executeRule(self, c, size, isNextOccupied):
        print("executing rule Eight.....")
        if (0 == c.getRow()) and (c.getColumn() < size - 1):
            print(
                "Rule Eight succeeds - current r/c:" + str(c.getRow()) + "/" + str(c.getColumn()) + " next r/c:" + str(
                    (size - 1)) + "/" + str(c.getColumn() + 1))
            return RowColumn(size - 1, c.getColumn() + 1)
        else:
            print("Rule Eight fails - current r/c: " + str(c.getRow()) + "/" + str(c.getColumn()))
            return RowColumn(-3, -3)
