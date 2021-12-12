import math
from expression_evaluator.token import *

class SquareRoot(Operator):
    type = TokenType.AdvanceOperator | TokenType.Variable
    symbols = ['sqrt']

    @classmethod
    def _function(cls, a):
        return math.sqrt(a)