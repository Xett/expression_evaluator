import math
from expression_evaluator.token import *

class PIOperator(Operator):
    type: TokenType = TokenType.Constant | TokenType.Variable
    symbols: list = ['PI']

    def _function():
        return math.pi