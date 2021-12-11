from expression_evaluator.token import Operator

class NotEqual(Operator):
    symbols: list = ['!=']

    def _function(a, b):
        return a != b