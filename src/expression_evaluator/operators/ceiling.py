import math
from expression_evaluator.types import *

class Ceiling(Operator):
    label: str = 'ceil'
    description: str = 'ceiling'
    symbols: list = ['ceil']
    type: OperatorType = OperatorType.Advanced | OperatorType.Value

    def _function(a):
        return math.ceil(a)