import math
from expression_evaluator.token import *

class ACosOperator(Operator):
    type = TokenType.AdvanceOperator | TokenType.Variable
    symbols = ['acos']

    @classmethod
    def _function(cls, a):
        return math.acos(a)