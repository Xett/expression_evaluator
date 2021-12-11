from expression_evaluator.token import *

class Negative(Operator):
    type: TokenType = TokenType.AdvanceOperator
    symbols: list = ['-']

    def _function(a):
        return -a