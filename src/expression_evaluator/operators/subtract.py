from expression_evaluator.types import *

class Subtract(Operator):
    label: str = 'sub'
    description: str = 'subtraction'
    symbols: list = ['-']

    def _function(a, b):
        return a - b