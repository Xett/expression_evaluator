import math
from expression_evaluator.token import *

class TanOperator(AdvanceOperator):
    symbols = ['tan']

    @classmethod    
    def _function(cls, a):
        return math.tan(a)