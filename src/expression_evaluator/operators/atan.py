import math
from expression_evaluator.token import *

class ATanOperator(Operator):
    type: TokenType = TokenType.AdvanceOperator | TokenType.Variable
    symbols: list = ['atan']

    def _function(a):
        return math.atan(a)