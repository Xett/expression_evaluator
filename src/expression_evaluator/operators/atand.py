import math
from expression_evaluator.types import *

class ATanDOperator(Operator):
    label: str = 'atand'
    description: str = 'atand'
    symbols: list = ['atand']
    type: OperatorType = OperatorType.Advanced

    def _function(a):
        return math.degrees(math.atan(a))