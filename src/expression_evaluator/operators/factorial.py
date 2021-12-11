import math
from expression_evaluator.token import *

class Factorial(Operator):
    type: TokenType = TokenType.Function | TokenType.Variable
    symbols: list = ['fac']

    def _function(a):
        return math.factorial(a)