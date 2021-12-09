from expression_evaluator import *
from expression_evaluator.types import Operator

class NotEqual(Operator):
    label: str = 'notEqual'
    description: str = 'not equal'
    symbols: list = ['!=']

    def _function(a, b):
        return a != b