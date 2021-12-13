from expression_evaluator.token import *

class Subtract(BasicOperator):
    symbols = ['-']
    priority = 4

    @classmethod
    def _function(cls, a, b):
        return a - b