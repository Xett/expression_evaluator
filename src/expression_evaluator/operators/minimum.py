from expression_evaluator.types import *

class Minimum(Operator):
    label: str = 'minimum'
    description: str = 'minimum'
    symbols: list = ['min']
    type: OperatorType = OperatorType.Function | OperatorType.Value

    def _function(a):
        return min(a)