from expression_evaluator.token import *

class Minimum(AdvanceOperator):
    symbols = ['min']

    @classmethod
    def _function(cls, a):
        return min(a)