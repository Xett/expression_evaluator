from expression_evaluator.token import *

class NotOperator(AdvanceOperator):
    symbols = ['not']
    priority = 2

    @classmethod
    def _function(a):
        return not a