import math
from expression_evaluator.token import *

class TanDOperator(Operator):
    type: TokenType = TokenType.AdvanceOperator
    symbols: list = ['tand']

    def _function(a):
        return math.tan(math.radians(a))