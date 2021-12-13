import math
from expression_evaluator.token import *

class SquareRoot(AdvanceOperator):
    symbols = ['sqrt']

    @classmethod
    def _function(cls, a):
        return math.sqrt(a)