import math
from expression_evaluator.token import *

class SinOperator(Operator):
    type: TokenType = TokenType.AdvanceOperator | TokenType.Variable
    symbols: list = ['sin']

    def _function(a):
        return math.sin(a)