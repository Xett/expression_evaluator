from expression_evaluator.token import *

class Negative(AdvanceOperator):
    is_sign = True
    symbols = ['-']
    priority = PriorityLevel.Sign

    @classmethod
    def _function(cls, a):
        return -a