from expression_evaluator.token import *

class Maximum(AdvanceOperator):
    symbols = ['max']

    @classmethod
    def _function(a):
        return max(a)