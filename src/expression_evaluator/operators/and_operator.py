from expression_evaluator.token import *

class AndOperator(BasicOperator):
    symbols = ['and']
    priority = 1

    @classmethod
    def _function(cls, a, b):
        return (a and b)