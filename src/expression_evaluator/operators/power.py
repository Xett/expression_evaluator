from expression_evaluator.token import *

class Power(Operator):
    symbols: list = ['^', '**']
    priority: int = 8

    def _function(a, b):
        return a ** b