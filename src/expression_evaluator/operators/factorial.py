import math
from expression_evaluator.token import *

class Factorial(AdvanceOperator):
    symbols = ['fac']

    @classmethod
    def _function(cls, a):
        return math.factorial(a)