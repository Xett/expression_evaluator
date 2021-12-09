import random
from expression_evaluator.types import *

class Random(Operator):
    label: str = 'random'
    description: str = 'random'
    symbols: list = ['random']
    type: OperatorType = OperatorType.Function | OperatorType.Value

    def _function(a):
        return random.random() * (a or 1)