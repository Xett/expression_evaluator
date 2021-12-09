from expression_evaluator import *
from expression_evaluator.types import Operator

class Equal(Operator):
    label: str = 'equal'
    description: str = 'equal'
    symbols: list = ['==']

    def _function(a, b):
        return a == b