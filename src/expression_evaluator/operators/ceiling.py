import math
from expression_evaluator.token import *

class Ceiling(Operator):
    type: TokenType = TokenType.AdvanceOperator | TokenType.Variable
    symbols: list = ['ceil']

    def _function(a):
        return math.ceil(a)