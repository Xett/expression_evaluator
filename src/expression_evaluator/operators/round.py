from expression_evaluator.token import *

class ASinDOperator(AdvanceOperator):
    symbols = ['round']

    @classmethod
    def _function(cls, a):
        return round(a)