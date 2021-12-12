from expression_evaluator.token import *

class AndOperator(Operator):
    symbols: list = ['and']
    priority: int = 1

    def _function(a, b):
        return (a and b)