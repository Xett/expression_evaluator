import random
from expression_evaluator.token import *

class RollOperator(BasicOperator):
    symbols = ['D']
    priority = 1

    @classmethod
    def _function(cls, a, b):
        rolls = []
        roll = 0
        final = 0
        for c in range(1, a):
            roll = random.randint(1, b)
            rolls.append(roll)
        return rolls