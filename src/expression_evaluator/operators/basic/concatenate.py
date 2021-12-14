from expression_evaluator.token import *

class Concatenate(BasicOperator):
    symbols = ['||']
    priority = PriorityLevel.String

    @classmethod
    def _function(cls, a, b,*args):
        result=u'{0}{1}'.format(a, b)
        for arg in args:
            result=u'{0}{1}'.format(result, arg)
        return result