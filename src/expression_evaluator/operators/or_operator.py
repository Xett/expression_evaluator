from expression_evaluator.token import *

class OrOperator(Operator):
    symbols: list = ['or']
    priority: int = 0

    def _function(a, b):
        return (a or b)