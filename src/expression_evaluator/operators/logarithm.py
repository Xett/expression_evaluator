import math
from expression_evaluator.token import *

class Logarithm(Operator):
    type: TokenType = TokenType.Function | TokenType.Variable
    symbols: list = ['log']

    def _function(a):
        return math.log(a)