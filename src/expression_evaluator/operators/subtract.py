from expression_evaluator.token import *

class Subtract(Operator):
    symbols: list = ['-']

    def _function(a, b):
        return a - b