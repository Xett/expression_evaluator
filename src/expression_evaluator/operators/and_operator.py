from expression_evaluator.token import *

class AndOperator(Operator):
    symbols: list = ['and']

    def _function(a, b):
        return (a and b)