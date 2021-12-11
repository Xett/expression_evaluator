from expression_evaluator.token import *

class Equal(Operator):
    symbols: list = ['==']

    def _function(a, b):
        return a == b