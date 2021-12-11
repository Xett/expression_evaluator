from expression_evaluator.token import *

class Maximum(Operator):
    type: TokenType = TokenType.Function | TokenType.Variable
    symbols: list = ['max']

    def _function(a):
        return max(a)