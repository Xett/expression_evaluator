import math
from expression_evaluator.types import *

class ATanOperator(Operator):
    label: str = 'atan'
    description: str = 'atan'
    symbols: list = ['atan']
    type: OperatorType = OperatorType.Advanced | OperatorType.Value

    def _function(a):
        return math.atan(a)