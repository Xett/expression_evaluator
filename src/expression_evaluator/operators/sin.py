import math
from expression_evaluator.types import *

class SinOperator(Operator):
    label: str = 'sin'
    description: str = 'sin'
    symbols: list = ['sin']
    type: OperatorType = OperatorType.Advanced | OperatorType.Value

    def _function(a):
        return math.sin(a)