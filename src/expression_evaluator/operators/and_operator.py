from expression_evaluator import *
from expression_evaluator.types import Operator

class AndOperator(Operator):
    label: str = 'andOperator'
    description: str = 'and operator'
    symbols: list = ['and']

    def _function(a, b):
        return (a and b)