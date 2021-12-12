import math
from expression_evaluator.token import *

class Ceiling(Operator):
    type = TokenType.AdvanceOperator | TokenType.Variable
    symbols = ['ceil']

    @classmethod
    def _function(cls, a):
        return math.ceil(a)