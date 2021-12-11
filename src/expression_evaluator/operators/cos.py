import math
from expression_evaluator.token import *

class CosOperator(Operator):
    type: TokenType = TokenType.AdvanceOperator | TokenType.Variable
    symbols: list = ['cos']
    
    def _function(a):
        return math.cos(a)