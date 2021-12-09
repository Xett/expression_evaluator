import math
from expression_evaluator.types import *

class Floor(Operator):
    label: str = 'floor'
    description: str = 'floor'
    symbols: list = ['floor']
    type: OperatorType = OperatorType.Advanced | OperatorType.Value

    def _function(a):
        return math.floor(a)