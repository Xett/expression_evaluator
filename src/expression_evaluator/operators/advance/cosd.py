import math
from expression_evaluator.token import *

class CosDOperator(AdvanceOperator):
    symbols = ['cosd']


    @classmethod
    def _function(cls, a):
        return math.cos(math.radians(a))