import math
from expression_evaluator.token import *

class ACosDOperator(Operator):
    type = TokenType.AdvanceOperator
    symbols = ['acosd']

    @classmethod
    def _function(cls, a):
        return math.degrees(math.acos(a))