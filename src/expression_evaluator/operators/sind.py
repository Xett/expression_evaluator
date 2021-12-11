import math
from expression_evaluator.token import *

class SinDOperator(Operator):
    type: TokenType = TokenType.AdvanceOperator
    symbols: list = ['sind']

    def _function(a):
        return math.sin(math.radians(a))