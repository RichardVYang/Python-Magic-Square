from rowColumn import RowColumn


class RuleSix:

    def __init__(self):
        print("Initializing RuleSix...")

    def executeRule(self, c, size, isNextOccupied):
        print("executing rule Six.....")
        if (isNextOccupied) and (c.getRow() > 0) and (c.getColumn() < size - 1):
            print("Rule Six succeeds - current r/c:" + str(c.getRow()) + "/" + str(c.getColumn()) + " next r/c:" + str(
                (c.getRow() + 1)) + "/" + str(c.getColumn()))
            return RowColumn(c.getRow() + 1, c.getColumn())
        else:
            print("Rule Six fails - current r/c: " + str(c.getRow()) + "/" + str(c.getColumn()))
            return RowColumn(-3, -3)
