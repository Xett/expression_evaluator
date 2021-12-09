import math
from expression_evaluator.types import *

class ACosOperator(Operator):
    label: str = 'acos'
    description: str = 'acos'
    symbols: list = ['acos']
    type: OperatorType = OperatorType.Advanced | OperatorType.Value

    def _function(a):
        return math.acos(a)