import math
from expression_evaluator.types import *

class EOperator(Operator):
    label: str = 'E'
    description: str = 'E'
    symbols: list = ['E']
    type: OperatorType = OperatorType.Constant | OperatorType.Value

    def _function():
        return math.e