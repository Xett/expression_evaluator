import math
from expression_evaluator.token import *

class ASinOperator(AdvanceOperator):
    symbols = ['asin']
    
    @classmethod
    def _function(cls, a):
        return math.asin(a)