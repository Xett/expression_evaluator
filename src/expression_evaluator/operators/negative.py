from expression_evaluator.types import *

class Negative(Operator):
    label: str = 'neg'
    description: str = 'negative'
    symbols: list = ['-']
    type: OperatorType = OperatorType.Advanced

    def _function(a):
        return -a