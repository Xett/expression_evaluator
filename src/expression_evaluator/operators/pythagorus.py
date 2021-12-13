import math
from expression_evaluator.token import *

class Pythagorus(BasicOperator):
    symbols = ['pyt']

    @classmethod
    def _function(cls, a, b):
        return math.sqrt(a*a + b*b)