import math
from expression_evaluator.token import *

class TanDOperator(AdvanceOperator):
    symbols = ['tand']

    @classmethod
    def _function(cls, a):
        return math.tan(math.radians(a))