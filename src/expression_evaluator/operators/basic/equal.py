from expression_evaluator.token import *

class Equal(BasicOperator):
    symbols = ['==']
    priority = PriorityLevel.Boolean

    @classmethod
    def _function(cls, a, b):
        return a == b