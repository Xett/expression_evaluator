import math
from expression_evaluator.token import *

class SquareRoot(Operator):
    type: TokenType = TokenType.AdvanceOperator | TokenType.Variable
    symbols: list = ['sqrt']

    def _function(a):
        return math.sqrt(a)