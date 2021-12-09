import math
from expression_evaluator.types import *

class ASinOperator(Operator):
    label: str = 'asin'
    description: str = 'asin'
    symbols: list = ['asin']
    type: OperatorType = OperatorType.Advanced | OperatorType.Value

    def _function(a):
        return math.asin(a)