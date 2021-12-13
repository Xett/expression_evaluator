import math
from expression_evaluator.token import *

class Floor(AdvanceOperator):
    symbols = ['floor']

    @classmethod
    def _function(cls, a):
        return math.floor(a)