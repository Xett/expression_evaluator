from expression_evaluator.types import *

class Maximum(Operator):
    label: str = 'maximum'
    description: str = 'maximum'
    symbols: list = ['max']
    type: OperatorType = OperatorType.Function | OperatorType.Value

    def _function(a):
        return max(a)