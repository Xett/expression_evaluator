from expression_evaluator.token import *

class OrOperator(Operator):
    symbols = ['or']
    priority = 0

    @classmethod
    def _function(cls, a, b):
        return (a or b)