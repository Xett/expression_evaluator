from expression_evaluator.token import *

class Add(Operator):
    symbols: list = ['+']

    def _function(a, b):
        return a + b