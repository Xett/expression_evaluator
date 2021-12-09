from expression_evaluator.types import *

class InOperator(Operator):
    label: str = 'inOperator'
    description: str = 'in operator'
    symbols: list = ['in']

    def _function(a, b):
        return a in b