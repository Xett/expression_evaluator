from expression_evaluator.token import *

class Negative(Operator):
    type: TokenType = TokenType.AdvanceOperator
    is_sign: bool = True
    symbols: list = ['-']
    priority: int = 5

    def _function(a):
        return -a