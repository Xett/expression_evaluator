from expression_evaluator.token import *

class Divide(Operator):
    symbols: list = ['/']

    def _function(a, b):
        return a / b