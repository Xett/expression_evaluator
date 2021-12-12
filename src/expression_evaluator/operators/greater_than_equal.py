from expression_evaluator.token import Operator

class GreaterThanEqual(Operator):
    symbols = ['>=']
    priority = 3

    @classmethod
    def _function(cls, a, b):
        return a >= b