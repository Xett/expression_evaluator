import math
from expression_evaluator.types import *

class MathPower(Operator):
    label: str = 'mathPower'
    description: str = 'math implementation of power'
    symbols: list = ['pow']
    type: OperatorType = OperatorType.Function | OperatorType.Value

    def _function(a):
        return math.pow(a)