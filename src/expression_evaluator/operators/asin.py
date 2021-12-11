import math
from expression_evaluator.token import *

class ASinOperator(Operator):
    type: TokenType = TokenType.AdvanceOperator | TokenType.Variable
    symbols: list = ['asin']
    
    def _function(a):
        return math.asin(a)