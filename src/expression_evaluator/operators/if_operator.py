import math
from expression_evaluator.types import *

class IfOperator(Operator):
    label: str = 'if'
    description: str = 'if'
    symbols: list = ['if']
    type: OperatorType = OperatorType.Function

    def _function(a, b, c):
        return b if a else c