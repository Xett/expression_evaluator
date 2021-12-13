from expression_evaluator.token import *

class InOperator(BasicOperator):
    symbols = ['in']
    priority = 3

    @classmethod
    def _function(cls, a, b):
        return a in b