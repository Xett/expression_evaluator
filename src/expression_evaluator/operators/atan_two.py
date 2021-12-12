import math
from expression_evaluator.token import *

class ATanTwo(Operator):
    type = TokenType.Function | TokenType.Variable
    symbols = ['atan2']

    @classmethod
    def _function(cls, a):
        return math.atan2(a)