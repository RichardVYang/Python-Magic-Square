from rowColumn import RowColumn


class RuleThree:

    def __init__(self):
        print("Initializing RuleThree...")

    def executeRule(self, c, size, isNextOccupied):
        print("executing rule three.....")
        if (not isNextOccupied) and (c.getColumn() + 1 < size) and (c.getRow() - 1 >= 0):
            print(
                "Rule Three succeeds - current r/c:" + str(c.getRow()) + "/" + str(c.getColumn()) + " next r/c:" + str(
                    (c.getRow() - 1)) + "/" + str(c.getColumn() + 1))
            return RowColumn(c.getRow() - 1, c.getColumn() + 1)
        else:
            print("Rule Three fails - current r/c: " + str(c.getRow()) + "/" + str(c.getColumn()))
            return RowColumn(-3, -3)
