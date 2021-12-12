from expression_evaluator.token import *

class Power(Operator):
    symbols = ['^', '**']
    priority = 8

    @classmethod
    def _function(cls, a, b):
        return a ** b