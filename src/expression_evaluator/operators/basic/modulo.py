from expression_evaluator.token import *

class Modulo(BasicOperator):
    symbols = ['%']
    priority = PriorityLevel.Divide

    @classmethod
    def _function(a, b):
        return a % b