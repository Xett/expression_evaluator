from expression_evaluator.token import *

class Multiply(Operator):
    symbols: list = ['*']

    def _function(a, b):
        return a * b