from expression_evaluator.token import *

class XorOperator(Operator):
    symbols: list = ['xor']
    priority: int = 0

    def _function(a, b):
        return (a^b)