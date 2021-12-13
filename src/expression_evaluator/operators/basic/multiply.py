from expression_evaluator.token import *

class Multiply(BasicOperator):
    symbols = ['*']
    priority = 5

    @classmethod
    def _function(cls, a, b):
        return a * b