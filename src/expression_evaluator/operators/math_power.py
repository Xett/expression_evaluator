import math
from expression_evaluator.token import *

class MathPower(Operator):
    type = TokenType.Function | TokenType.Variable
    symbols = ['pow']

    @classmethod
    def _function(cls, a):
        return math.pow(a)