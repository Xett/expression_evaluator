from expression_evaluator.token import *

class Concatenate(Operator):
    type: TokenType = TokenType.BasicOperator | TokenType.Function
    symbols = ['||']
    priority = 3

    @classmethod
    def _function(cls, a, b,*args):
        result=u'{0}{1}'.format(a, b)
        for arg in args:
            result=u'{0}{1}'.format(result, arg)
        return result