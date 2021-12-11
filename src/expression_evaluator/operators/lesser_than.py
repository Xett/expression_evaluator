from expression_evaluator.token import *

class LesserThan(Operator):
    symbols: list = ['<']

    def _function(a, b):
        return a < b