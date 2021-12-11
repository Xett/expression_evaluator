import math
from expression_evaluator.token import *

class IfOperator(Operator):
    type: TokenType = TokenType.Function
    symbols: list = ['if']

    def _function(a, b, c):
        return b if a else c