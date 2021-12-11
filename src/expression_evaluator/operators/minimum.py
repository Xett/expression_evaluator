from expression_evaluator.token import *

class Minimum(Operator):
    type: TokenType = TokenType.Function | TokenType.Variable
    symbols: list = ['min']

    def _function(a):
        return min(a)