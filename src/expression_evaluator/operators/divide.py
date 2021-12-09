from expression_evaluator.types import *

class Divide(Operator):
    label: str = 'div'
    description: str = 'divide'
    symbols: list = ['/']

    def _function(a, b):
        return a / b