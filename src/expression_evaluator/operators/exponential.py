import math
from expression_evaluator.token import *

class Exponential(Operator):
    type = TokenType.AdvanceOperator | TokenType.Variable
    symbols = ['exp']

    @classmethod
    def _function(cls, a):
        return math.exp(a)