from expression_evaluator.types import *

class Append(Operator):
    label: str = 'append'
    description: str = 'append'
    symbols: list = [',']

    def _function(a, b):
        if type(a) != list:
            return [a, b]
        a.append(b)
        return a