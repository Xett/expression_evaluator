import math
from expression_evaluator.token import *

class ATanTwo(Operator):
    type: TokenType = TokenType.Function | TokenType.Variable
    symbols: list = ['atan2']

    def _function(a):
        return math.atan2(a)