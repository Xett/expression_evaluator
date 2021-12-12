from expression_evaluator.token import *

class Minimum(Operator):
    type = TokenType.Function | TokenType.Variable
    symbols = ['min']

    @classmethod
    def _function(cls, a):
        return min(a)