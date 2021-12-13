import math
from expression_evaluator.token import *

class ATanTwo(AdvanceOperator):
    symbols = ['atan2']

    @classmethod
    def _function(cls, a):
        return math.atan2(a)