import math
from expression_evaluator.types import *

class ACosDOperator(Operator):
    label: str = 'acosd'
    description: str = 'acosd'
    symbols: list = ['acosd']
    type: OperatorType = OperatorType.Advanced

    def _function(a):
        return math.degrees(math.acos(a))