import math
from expression_evaluator.token import *

class ATanOperator(Operator):
    type = TokenType.AdvanceOperator | TokenType.Variable
    symbols = ['atan']

    @classmethod
    def _function(cls, a):
        return math.atan(a)