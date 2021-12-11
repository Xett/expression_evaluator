from expression_evaluator.token import *

class XorOperator(Operator):
    symbols: list = ['xor']

    def _function(a, b):
        return (a^b)