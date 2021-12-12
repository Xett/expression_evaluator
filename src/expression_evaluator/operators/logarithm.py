import math
from expression_evaluator.token import *

class Logarithm(Operator):
    type = TokenType.Function | TokenType.Variable
    symbols = ['log']

    @classmethod
    def _function(cls, a):
        return math.log(a)