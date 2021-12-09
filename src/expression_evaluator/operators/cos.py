import math
from expression_evaluator.types import *

class CosOperator(Operator):
    label: str = 'cos'
    description: str = 'cos'
    symbols: list = ['cos']
    type: OperatorType = OperatorType.Advanced | OperatorType.Value

    def _function(a):
        return math.cos(a)