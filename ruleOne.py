# rule one

from rowColumn import RowColumn


class RuleOne:

    """
    The constructor method below doesn't do any initialization besides print that single line for info purpose.
    All the rules can be changed to class functions instead of class instance methods.
    """
    def __init__(self):
        print("Initializing RuleOne...")

    def executeRule(self, c, size, isNextOccupied):
        print("executing rule one.....")

        if (-1 == c.getRow()) and (-1 == c.getColumn()):
            print("Rule One succeeds - current r/c: " + str(c.getRow()) + "/" + str(c.getColumn()) + " next r/c:" + str(
                0) + "/" + str((size // 2)))
            return RowColumn(0, size // 2)
        else:
            print("Rule One fails - current r/c: " + str(c.getRow()) + "/" + str(c.getColumn()))
            return RowColumn(-3, -3)
