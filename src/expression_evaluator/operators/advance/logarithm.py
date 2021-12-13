import math
from expression_evaluator.token import *

class Logarithm(AdvanceOperator):
    symbols = ['log']

    @classmethod
    def _function(cls, a):
        return math.log(a)