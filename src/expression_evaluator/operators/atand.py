import math
from expression_evaluator.token import *

class ATanDOperator(Operator):
    type = TokenType.AdvanceOperator
    symbols = ['atand']

    @classmethod
    def _function(cls, a):
        return math.degrees(math.atan(a))