from expression_evaluator import *
from expression_evaluator.types import Operator

class GreaterThanEqual(Operator):
    label: str = 'greaterThanEqual'
    description: str = 'greater than equal'
    symbols: list = ['>=']

    def _function(a, b):
        return a >= b