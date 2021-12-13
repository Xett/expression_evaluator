import math
from expression_evaluator.token import *

class Ceiling(AdvanceOperator):
    symbols = ['ceil']

    @classmethod
    def _function(cls, a):
        return math.ceil(a)