import math
from expression_evaluator.token import *

class ASinDOperator(Operator):
    type: TokenType = TokenType.AdvanceOperator
    symbols: list = ['asind']

    def _function(a):
        return math.degrees(math.asin(a))