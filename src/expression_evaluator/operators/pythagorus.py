import math
from expression_evaluator.token import *

class Pythagorus(Operator):
    type = TokenType.Function | TokenType.Variable
    symbols = ['pyt']

    @classmethod
    def _function(cls, a, b):
        return math.sqrt(a*a + b*b)