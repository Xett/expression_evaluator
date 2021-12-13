from expression_evaluator.token import *

class Divide(BasicOperator):
    symbols = ['/']
    priority = 6

    @classmethod
    def _function(cls, a, b):
        return a / b