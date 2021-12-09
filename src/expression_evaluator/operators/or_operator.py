from expression_evaluator import *
from expression_evaluator.types import Operator

class OrOperator(Operator):
    label: str = 'orOperator'
    description: str = 'or operator'
    symbols: list = ['or']

    def _function(a, b):
        return (a or b)