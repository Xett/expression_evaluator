from expression_evaluator.token import *

class Absolute(Operator):
    type = TokenType.AdvanceOperator | TokenType.Variable
    symbols = ['abs']

    @classmethod
    def _function(cls, a):
        return abs(a)