import math
from expression_evaluator.types import *

class ATanTwo(Operator):
    label: str = 'atan2'
    description: str = 'math atan2'
    symbols: list = ['atan2']
    type: OperatorType = OperatorType.Function | OperatorType.Value

    def _function(a):
        return math.atan2(a)