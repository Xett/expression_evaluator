from expression_evaluator.types import *

class Divide(Operator):
    label: str = 'div'
    description: str = 'divide'
    symbol: str = '/'

    def _function(a, b):
        return a / b