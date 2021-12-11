from expression_evaluator.token import *

class NotOperator(Operator):
    type: TokenType = TokenType.AdvanceOperator
    symbols: list = ['not']

    def _function(a):
        return not a