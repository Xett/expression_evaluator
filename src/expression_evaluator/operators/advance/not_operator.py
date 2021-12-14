from expression_evaluator.token import *

class NotOperator(AdvanceOperator):
    symbols = ['not']
    priority = PriorityLevel.Not

    @classmethod
    def _function(a):
        return not a