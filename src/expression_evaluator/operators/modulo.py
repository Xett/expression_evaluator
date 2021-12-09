from expression_evaluator.types import *

class Modulo(Operator):
    label: str = 'mod'
    description: str = 'modulo'
    symbols: list = ['%']

    def _function(a, b):
        return a % b