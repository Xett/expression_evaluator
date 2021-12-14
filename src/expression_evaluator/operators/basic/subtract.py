from expression_evaluator.token import *

class Subtract(BasicOperator):
    symbols = ['-']
    priority = PriorityLevel.Subtract

    @classmethod
    def _function(cls, a, b):
        return a - b