from expression_evaluator.types import *

class Multiply(Operator):
    label: str = 'mul'
    description: str = 'multiply'
    symbols: list = ['*']


    def _function(a, b):
        return a * b