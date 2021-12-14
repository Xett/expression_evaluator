from expression_evaluator.token import *

class AndOperator(BasicOperator):
    symbols = ['and']
    priority = PriorityLevel.And

    @classmethod
    def _function(cls, a, b):
        return (a and b)