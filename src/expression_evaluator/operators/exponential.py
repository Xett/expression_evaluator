import math
from expression_evaluator.token import *

class Exponential(Operator):
    type: TokenType = TokenType.AdvanceOperator | TokenType.Variable
    symbols: list = ['exp']

    def _function(a):
        return math.exp(a)