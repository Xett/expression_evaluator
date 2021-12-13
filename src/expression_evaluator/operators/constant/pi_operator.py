import math
from expression_evaluator.token import *

class PIOperator(ConstantOperator):
    symbols = ['PI']

    @classmethod
    def _function(cls):
        return math.pi