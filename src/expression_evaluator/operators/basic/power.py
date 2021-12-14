from expression_evaluator.token import *

class Power(BasicOperator):
    symbols = ['^', '**']
    priority = PriorityLevel.Power

    @classmethod
    def _function(cls, a, b):
        return a ** b