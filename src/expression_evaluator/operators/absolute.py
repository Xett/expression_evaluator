from expression_evaluator.token import *

class Absolute(Operator):
    type = TokenType.AdvanceOperator | TokenType.Variable
    symbols: list = ['abs']

    def _function(a):
        return abs(a)