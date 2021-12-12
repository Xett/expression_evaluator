import math
from expression_evaluator.token import *

class CosDOperator(Operator):
    type = TokenType.AdvanceOperator
    symbols = ['cosd']


    @classmethod
    def _function(cls, a):
        return math.cos(math.radians(a))