from expression_evaluator.token import *

class LesserThanEqual(Operator):
    symbols: list = ['<=']
    priority: int = 3

    def _function(a, b):
        return a <= b