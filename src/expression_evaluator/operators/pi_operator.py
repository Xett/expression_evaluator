import math
from expression_evaluator.token import *

class PIOperator(Operator):
    type = TokenType.Constant | TokenType.Variable
    symbols = ['PI']

    @classmethod
    def _function(cls):
        return math.pi