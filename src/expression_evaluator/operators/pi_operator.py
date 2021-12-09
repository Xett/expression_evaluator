import math
from expression_evaluator.types import *

class PIOperator(Operator):
    label: str = 'PI'
    description: str = 'PI'
    symbols: list = ['PI']
    type: OperatorType = OperatorType.Constant | OperatorType.Value

    def _function():
        return math.pi