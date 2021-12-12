import math
from expression_evaluator.token import *

class TanOperator(Operator):
    type = TokenType.AdvanceOperator | TokenType.Variable
    symbols = ['tan']

    @classmethod    
    def _function(cls, a):
        return math.tan(a)