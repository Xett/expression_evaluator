from expression_evaluator.token import *

class Maximum(Operator):
    type = TokenType.Function | TokenType.Variable
    symbols = ['max']

    @classmethod
    def _function(a):
        return max(a)