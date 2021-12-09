import math
from expression_evaluator.types import *

class Logarithm(Operator):
    label: str = 'logarithm'
    description: str = 'logarithm'
    symbols: list = ['log']
    type: OperatorType = OperatorType.Function | OperatorType.Value

    def _function(a):
        return math.log(a)