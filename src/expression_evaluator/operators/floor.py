import math
from expression_evaluator.token import *

class Floor(Operator):
    type = TokenType.AdvanceOperator | TokenType.Variable
    symbols = ['floor']

    @classmethod
    def _function(cls, a):
        return math.floor(a)