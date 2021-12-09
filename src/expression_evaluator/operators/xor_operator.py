from expression_evaluator import *
from expression_evaluator.types import Operator

class XorOperator(Operator):
    label: str = 'xorOperator'
    description: str = 'xor operator'
    symbols: list = ['xor']

    def _function(a, b):
        return (a^b)