import math
from expression_evaluator.types import *

class Factorial(Operator):
    label: str = 'factorial'
    description: str = 'factorial'
    symbols: list = ['fac']
    type: OperatorType = OperatorType.Function | OperatorType.Value

    def _function(a):
        return math.factorial(a)