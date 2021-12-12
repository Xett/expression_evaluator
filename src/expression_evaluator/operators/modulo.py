from expression_evaluator.token import *

class Modulo(Operator):
    symbols: list = ['%']
    priority: int = 6

    def _function(a, b):
        return a % b