from expression_evaluator.token import *

class InOperator(Operator):
    symbols: list = ['in']
    priority: int = 3

    def _function(a, b):
        return a in b