from expression_evaluator.token import *

class InOperator(Operator):
    symbols: list = ['in']

    def _function(a, b):
        return a in b