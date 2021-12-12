from expression_evaluator.token import *

class Equal(Operator):
    symbols = ['==']
    priority = 3

    @classmethod
    def _function(cls, a, b):
        return a == b