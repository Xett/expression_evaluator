import math
from expression_evaluator.token import *

class EOperator(Operator):
    type = TokenType.Constant | TokenType.Variable
    symbols = ['E']

    @classmethod
    def _function(cls):
        return math.e