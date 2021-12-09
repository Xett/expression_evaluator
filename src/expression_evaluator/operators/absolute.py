from expression_evaluator.types import *

class Absolute(Operator):
    label: str = 'abs'
    description: str = 'absolute'
    symbols: list = ['abs']
    type: OperatorType = OperatorType.Advanced | OperatorType.Value

    def _function(a):
        return abs(a)