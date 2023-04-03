from rowColumn import RowColumn


class RuleSeven:

    def __init__(self):
        print("Initializing RuleSeven...")

    def executeRule(self, c, size, isNextOccupied):
        print("executing rule Seven.....")
        if (not isNextOccupied) and (c.getRow() > 0) and (c.getColumn() < size - 1):
            print(
                "Rule Seven succeeds - current r/c:" + str(c.getRow()) + "/" + str(c.getColumn()) + " next r/c:" + str(
                    (c.getRow() + 1)) + "/" + str(c.getColumn()))
            return RowColumn(c.getRow() + 1, c.getColumn())
        else:
            print("Rule Seven fails - current r/c: " + str(c.getRow()) + "/" + str(c.getColumn()))
            return RowColumn(-3, -3)
