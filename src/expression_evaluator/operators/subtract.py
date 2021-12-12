from expression_evaluator.token import *

class Subtract(Operator):
    symbols: list = ['-']
    priority: int = 4

    def _function(a, b):
        return a - b