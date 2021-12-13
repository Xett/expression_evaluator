import math
from expression_evaluator.token import *

class ASinDOperator(AdvanceOperator):
    symbols = ['asind']

    @classmethod
    def _function(cls, a):
        return math.degrees(math.asin(a))