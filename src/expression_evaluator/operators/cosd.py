import math
from expression_evaluator.token import *

class CosDOperator(Operator):
    type: TokenType = TokenType.AdvanceOperator
    symbols: list = ['cosd']

    def _function(a):
        return math.cos(math.radians(a))