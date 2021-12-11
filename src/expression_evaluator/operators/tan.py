import math
from expression_evaluator.token import *

class TanOperator(Operator):
    type: TokenType = TokenType.AdvanceOperator | TokenType.Variable
    symbols: list = ['tan']

    def _function(a):
        return math.tan(a)