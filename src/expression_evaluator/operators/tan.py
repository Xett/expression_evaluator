import math
from expression_evaluator.types import *

class TanOperator(Operator):
    label: str = 'tan'
    description: str = 'tan'
    symbols: list = ['tan']
    type: OperatorType = OperatorType.Advanced | OperatorType.Value

    def _function(a):
        return math.tan(a)