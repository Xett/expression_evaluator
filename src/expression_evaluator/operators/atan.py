import math
from expression_evaluator.token import *

class ATanOperator(AdvanceOperator):
    symbols = ['atan']

    @classmethod
    def _function(cls, a):
        return math.atan(a)