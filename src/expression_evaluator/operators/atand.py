import math
from expression_evaluator.token import *

class ATanDOperator(Operator):
    type: TokenType = TokenType.AdvanceOperator
    symbols: list = ['atand']

    def _function(a):
        return math.degrees(math.atan(a))