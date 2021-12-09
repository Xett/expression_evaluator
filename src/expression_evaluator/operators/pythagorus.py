import math
from expression_evaluator.types import *

class Pythagorus(Operator):
    label: str = 'pythagorus'
    description: str = 'pythagorus'
    symbols: list = ['pyt']
    type: OperatorType = OperatorType.Function | OperatorType.Value

    def _function(a, b):
        return math.sqrt(a*a + b*b)