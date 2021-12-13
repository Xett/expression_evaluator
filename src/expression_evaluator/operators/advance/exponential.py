import math
from expression_evaluator.token import *

class Exponential(AdvanceOperator):
    symbols = ['exp']

    @classmethod
    def _function(cls, a):
        return math.exp(a)