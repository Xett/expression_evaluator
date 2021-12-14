from expression_evaluator.token import *

class OrOperator(BasicOperator):
    symbols = ['or']

    @classmethod
    def _function(cls, a, b):
        return (a or b)