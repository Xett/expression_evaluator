import math
from expression_evaluator.token import *

class MathPower(Operator):
    type: TokenType = TokenType.Function | TokenType.Variable
    symbols: list = ['pow']

    def _function(a):
        return math.pow(a)