import math
from expression_evaluator.token import *

class EOperator(Operator):
    type: TokenType = TokenType.Constant | TokenType.Variable
    symbols: list = ['E']

    def _function():
        return math.e