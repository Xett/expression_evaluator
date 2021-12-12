import math
from expression_evaluator.token import *

class ASinOperator(Operator):
    type = TokenType.AdvanceOperator | TokenType.Variable
    symbols = ['asin']
    
    @classmethod
    def _function(cls, a):
        return math.asin(a)