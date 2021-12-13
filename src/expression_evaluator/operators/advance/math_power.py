import math
from expression_evaluator.token import *

class MathPower(AdvanceOperator):
    symbols = ['pow']

    @classmethod
    def _function(cls, a):
        return math.pow(a)