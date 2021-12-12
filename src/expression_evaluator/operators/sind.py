import math
from expression_evaluator.token import *

class SinDOperator(Operator):
    type = TokenType.AdvanceOperator
    symbols = ['sind']

    @classmethod
    def _function(cls, a):
        return math.sin(math.radians(a))