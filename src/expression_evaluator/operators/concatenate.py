from expression_evaluator.token import *

class Concatenate(Operator):
    type: TokenType = TokenType.BasicOperator | TokenType.Function
    symbols: list = ['||']

    def _function(a, b,*args):
        result=u'{0}{1}'.format(a, b)
        for arg in args:
            result=u'{0}{1}'.format(result, arg)
        return result