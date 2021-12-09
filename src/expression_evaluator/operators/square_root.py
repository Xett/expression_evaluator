import math
from expression_evaluator.types import *

class SquareRoot(Operator):
    label: str = 'sqrt'
    description: str = 'square root'
    symbols: list = ['sqrt']
    type: OperatorType = OperatorType.Advanced | OperatorType.Value

    def _function(a):
        return math.sqrt(a)