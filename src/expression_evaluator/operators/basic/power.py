from expression_evaluator.token import *

class Power(BasicOperator):
    symbols = ['^', '**']
    priority = 8

    @classmethod
    def _function(cls, a, b):
        return a ** b