from expression_evaluator.token import *

class NotEqual(BasicOperator):
    symbols = ['!=']
    priority = 3

    @classmethod
    def _function(cls, a, b):
        return a != b