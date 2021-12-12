from expression_evaluator.token import *

class XorOperator(Operator):
    symbols = ['xor']
    priority = 0

    @classmethod
    def _function(cls, a, b):
        return (a^b)