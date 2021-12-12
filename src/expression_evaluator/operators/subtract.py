from expression_evaluator.token import *

class Subtract(Operator):
    symbols = ['-']
    priority = 4

    @classmethod
    def _function(cls, a, b):
        return a - b