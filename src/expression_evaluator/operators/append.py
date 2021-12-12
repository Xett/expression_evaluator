from expression_evaluator.token import *

class Append(Operator):
    symbols = [',']

    @classmethod
    def _function(cls, a, b):
        if type(a) != list:
            return [a, b]
        a.append(b)
        return a