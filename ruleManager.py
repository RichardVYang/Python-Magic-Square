
# ruleManager.py

#import ruleOne
from rowColumn import RowColumn

from ruleOne import RuleOne
from ruleTwo import RuleTwo
from ruleThree import RuleThree
from ruleFour import RuleFour
from ruleFive import RuleFive
from ruleSix import RuleSix
from ruleSeven import RuleSeven
from ruleEight import RuleEight
from ruleTopRightCorner import RuleTopRightCorner


class RuleManager:

    def __init__(self, msize):
        self.size = msize
        self.rules = dict()

        print('Rule Manager init size:', self.size)
        self.initializerules(self.rules)

    def initializerules(self, rules):
        print("RuleManager:: initializeAllRules:")

        rules[1] = RuleOne()
        rules[2] = RuleTwo()
        rules[3] = RuleThree()
        rules[4] = RuleFour()
        rules[5] = RuleFive()
        rules[6] = RuleSix()
        rules[7] = RuleSeven()
        rules[8] = RuleEight()
        rules[9] = RuleTopRightCorner()

    def getNextPosition(self, current, size, isNextOccupied):

        next = RowColumn(-1, -1)

        for rule in self.rules:
            next = self.rules[rule].executeRule(current, size, isNextOccupied)
            if (next.getRow() >= 0) and (next.getColumn() >= 0):
                break

        return next
git