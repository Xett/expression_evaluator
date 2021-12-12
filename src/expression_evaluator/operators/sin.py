import math
from expression_evaluator.token import *

class SinOperator(Operator):
    type = TokenType.AdvanceOperator | TokenType.Variable
    symbols = ['sin']

    @classmethod
    def _function(cls, a):
        return math.sin(a)