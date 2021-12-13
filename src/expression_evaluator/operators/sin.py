import math
from expression_evaluator.token import *

class SinOperator(AdvanceOperator):
    symbols = ['sin']

    @classmethod
    def _function(cls, a):
        return math.sin(a)