from expression_evaluator.token import *

class InOperator(BasicOperator):
    symbols = ['in']
    priority = PriorityLevel.String

    @classmethod
    def _function(cls, a, b):
        return a in b