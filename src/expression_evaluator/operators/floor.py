import math
from expression_evaluator.token import *

class Floor(Operator):
    type: TokenType = TokenType.AdvanceOperator | TokenType.Variable
    symbols: list = ['floor']

    def _function(a):
        return math.floor(a)