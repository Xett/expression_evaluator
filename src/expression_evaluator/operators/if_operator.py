import math
from expression_evaluator.token import *

class IfOperator(Operator):
    type = TokenType.Function
    symbols = ['if']

    @classmethod
    def _function(cls, a, b, c):
        return b if a else c