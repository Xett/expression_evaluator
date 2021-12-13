from expression_evaluator.token import *

class Negative(AdvanceOperator):
    is_sign = True
    symbols = ['-']
    priority = 5

    @classmethod
    def _function(cls, a):
        return -a