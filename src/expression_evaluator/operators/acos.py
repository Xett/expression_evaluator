import math
from expression_evaluator.token import *

class ACosOperator(Operator):
    type: TokenType = TokenType.AdvanceOperator | TokenType.Variable
    symbols: list = ['acos']

    def _function(a):
        return math.acos(a)