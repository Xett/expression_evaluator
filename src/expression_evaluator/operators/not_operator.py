from expression_evaluator.token import *

class NotOperator(Operator):
    type: TokenType = TokenType.AdvanceOperator
    symbols: list = ['not']
    priority: int = 2

    def _function(a):
        return not a