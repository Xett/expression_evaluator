from expression_evaluator.token import *

class Multiply(Operator):
    symbols: list = ['*']
    priority: int = 5

    def _function(a, b):
        return a * b