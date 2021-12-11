import math
from expression_evaluator.token import *

class Pythagorus(Operator):
    type: TokenType = TokenType.Function | TokenType.Variable
    symbols: list = ['pyt']

    def _function(a, b):
        return math.sqrt(a*a + b*b)