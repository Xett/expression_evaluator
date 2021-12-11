from expression_evaluator.token import *

class LesserThanEqual(Operator):
    symbols: list = ['<=']

    def _function(a, b):
        return a <= b