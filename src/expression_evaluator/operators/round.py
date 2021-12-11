from expression_evaluator.token import *

class ASinDOperator(Operator):
    type: TokenType = TokenType.AdvanceOperator | TokenType.Variable
    symbols: list = ['round']

    def _function(a):
        return round(a)