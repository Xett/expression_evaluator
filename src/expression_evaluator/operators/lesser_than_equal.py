from expression_evaluator import *
from expression_evaluator.types import Operator

class LesserThanEqual(Operator):
    label: str = 'lesserThanEqual'
    description: str = 'lesser than equal'
    symbols: list = ['<=']

    def _function(a, b):
        return a <= b