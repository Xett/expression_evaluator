from expression_evaluator.token import *

class Absolute(AdvanceOperator):
    symbols = ['abs']

    @classmethod
    def _function(cls, a):
        return abs(a)