import math
from expression_evaluator.token import *

class ACosOperator(AdvanceOperator):
    symbols = ['acos']

    @classmethod
    def _function(cls, a):
        return math.acos(a)