import math
from expression_evaluator.types import *

class SinDOperator(Operator):
    label: str = 'sind'
    description: str = 'sind'
    symbols: list = ['sind']
    type: OperatorType = OperatorType.Advanced

    def _function(a):
        return math.sin(math.radians(a))