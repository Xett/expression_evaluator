import math
from expression_evaluator.types import *

class CosDOperator(Operator):
    label: str = 'cosd'
    description: str = 'cosd'
    symbols: list = ['cosd']
    type: OperatorType = OperatorType.Advanced

    def _function(a):
        return math.cos(math.radians(a))