from expression_evaluator.token import *

class Add(Operator):
    is_sign: bool = True
    symbols: list = ['+']
    priority: int = 5

    def _function(a, b):
        return a + b