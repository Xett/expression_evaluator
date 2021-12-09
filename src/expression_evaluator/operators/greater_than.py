from expression_evaluator import *
from expression_evaluator.types import Operator

class GreaterThan(Operator):
    label: str = 'greaterThan'
    description: str = 'greater than'
    symbols: list = ['>']

    def _function(a, b):
        return a > b