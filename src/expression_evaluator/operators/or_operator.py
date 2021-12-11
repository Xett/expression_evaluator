from expression_evaluator.token import *

class OrOperator(Operator):
    symbols: list = ['or']

    def _function(a, b):
        return (a or b)