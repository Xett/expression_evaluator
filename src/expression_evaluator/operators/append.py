from expression_evaluator.token import *

class Append(Operator):
    symbols: list = [',']

    def _function(a, b):
        if type(a) != list:
            return [a, b]
        a.append(b)
        return a