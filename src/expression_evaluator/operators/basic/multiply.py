from expression_evaluator.token import *

class Multiply(BasicOperator):
    symbols = ['*']
    priority = PriorityLevel.Multiply

    @classmethod
    def _function(cls, a, b):
        return a * b