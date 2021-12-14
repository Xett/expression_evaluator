from expression_evaluator.token import *

class LesserThan(BasicOperator):
    symbols = ['<']
    priority = PriorityLevel.Boolean

    @classmethod
    def _function(cls, a, b):
        return a < b