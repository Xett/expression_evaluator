import math
from expression_evaluator.token import *

class CosOperator(Operator):
    type = TokenType.AdvanceOperator | TokenType.Variable
    symbols = ['cos']
    
    @classmethod
    def _function(cls, a):
        return math.cos(a)