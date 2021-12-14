from expression_evaluator.token import *

class XorOperator(BasicOperator):
    symbols = ['xor']

    @classmethod
    def _function(cls, a, b):
        return (a^b)