from expression_evaluator import *
from expression_evaluator.types import Operator

class LesserThan(Operator):
    label: str = 'lesserThan'
    description: str = 'lesser than'
    symbols: list = ['<']

    def _function(a, b):
        return a < b