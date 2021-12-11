from expression_evaluator.token import *

class Power(Operator):
    symbols: list = ['^', '**']

    def _function(a, b):
        return a ** b