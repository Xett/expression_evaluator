from expression_evaluator.token import *

class LesserThanEqual(BasicOperator):
    symbols = ['<=']
    priority = 3

    @classmethod
    def _function(cls, a, b):
        return a <= b