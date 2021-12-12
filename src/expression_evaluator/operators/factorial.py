import math
from expression_evaluator.token import *

class Factorial(Operator):
    type = TokenType.Function | TokenType.Variable
    symbols = ['fac']

    @classmethod
    def _function(cls, a):
        return math.factorial(a)