import math
from expression_evaluator.token import *

class ASinDOperator(Operator):
    type = TokenType.AdvanceOperator
    symbols = ['asind']

    @classmethod
    def _function(cls, a):
        return math.degrees(math.asin(a))