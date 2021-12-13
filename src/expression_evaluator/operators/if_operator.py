import math
from expression_evaluator.token import *

class IfOperator(AdvanceOperator):
    symbols = ['if']

    @classmethod
    def _function(cls, a, b, c):
        return b if a else c