import random
from expression_evaluator.token import *

class RollOperator(Operator):
    symbols: list = ['D']

    def _function(a, b):
        rolls = []
        roll = 0
        final = 0
        for c in range(1, a):
            roll = random.randint(1, b)
            rolls.append(roll)
        return rolls