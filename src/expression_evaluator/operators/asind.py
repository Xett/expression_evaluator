import math
from expression_evaluator.types import *

class ASinDOperator(Operator):
    label: str = 'asind'
    description: str = 'asind'
    symbols: list = ['asind']
    type: OperatorType = OperatorType.Advanced

    def _function(a):
        return math.degrees(math.asin(a))