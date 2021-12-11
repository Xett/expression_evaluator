import math
from expression_evaluator.token import *

class ACosDOperator(Operator):
    type: TokenType = TokenType.AdvanceOperator
    symbols: list = ['acosd']

    def _function(a):
        return math.degrees(math.acos(a))