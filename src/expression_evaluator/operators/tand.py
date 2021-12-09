import math
from expression_evaluator.types import *

class TanDOperator(Operator):
    label: str = 'tand'
    description: str = 'tand'
    symbols: list = ['tand']
    type: OperatorType = OperatorType.Advanced

    def _function(a):
        return math.tan(math.radians(a))