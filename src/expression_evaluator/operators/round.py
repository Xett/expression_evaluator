from expression_evaluator.types import *

class ASinDOperator(Operator):
    label: str = 'round'
    description: str = 'round'
    symbols: list = ['round']
    type: OperatorType = OperatorType.Advanced | OperatorType.Value

    def _function(a):
        return round(a)