from expression_evaluator.token import *

class Divide(BasicOperator):
    symbols = ['/']
    priority = PriorityLevel.Divide

    @classmethod
    def _function(cls, a, b):
        return a / b