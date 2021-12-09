import math
from expression_evaluator.types import *

class Exponential(Operator):
    label: str = 'exp'
    description: str = 'exponential'
    symbols: list = ['exp']
    type: OperatorType = OperatorType.Advanced | OperatorType.Value

    def _function(a):
        return math.exp(a)