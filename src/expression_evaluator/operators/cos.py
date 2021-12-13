import math
from expression_evaluator.token import *

class CosOperator(AdvanceOperator):
    symbols = ['cos']
    
    @classmethod
    def _function(cls, a):
        return math.cos(a)