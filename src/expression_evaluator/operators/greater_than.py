from expression_evaluator.token import Operator

class GreaterThan(Operator):
    symbols: list = ['>']

    def _function(a, b):
        return a > b