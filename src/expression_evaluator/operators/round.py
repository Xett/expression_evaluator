from expression_evaluator.token import *

class ASinDOperator(Operator):
    type = TokenType.AdvanceOperator | TokenType.Variable
    symbols = ['round']

    @classmethod
    def _function(cls, a):
        return round(a)