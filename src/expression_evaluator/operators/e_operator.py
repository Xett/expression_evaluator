import math
from expression_evaluator.token import *

class EOperator(ConstantOperator):
    symbols = ['E']

    @classmethod
    def _function(cls):
        return math.e