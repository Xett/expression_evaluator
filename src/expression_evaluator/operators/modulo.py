from expression_evaluator.token import *

class Modulo(Operator):
    symbols = ['%']
    priority = 6

    @classmethod
    def _function(a, b):
        return a % b