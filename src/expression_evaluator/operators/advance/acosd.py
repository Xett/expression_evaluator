import math
from expression_evaluator.token import *

class ACosDOperator(AdvanceOperator):
    symbols = ['acosd']

    @classmethod
    def _function(cls, a):
        return math.degrees(math.acos(a))