from expression_evaluator.types import *

class Power(Operator):
    label: str = 'pow'
    description: str = 'power'
    symbols: list = ['^', '**']

    def _function(a, b):
        return a ** b