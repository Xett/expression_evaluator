from expression_evaluator.token import *

class OrOperator(BasicOperator):
    symbols = ['or']
    priority = 0

    @classmethod
    def _function(cls, a, b):
        return (a or b)