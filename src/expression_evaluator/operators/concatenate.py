from expression_evaluator import *
from expression_evaluator.types import Operator, OperatorType

class Concatenate(Operator):
    label: str = 'concat'
    description: str = 'concatenate'
    symbols: list = ['||']
    type: OperatorType = OperatorType.Basic | OperatorType.Function

    def _function(a, b,*args):
        result=u'{0}{1}'.format(a, b)
        for arg in args:
            result=u'{0}{1}'.format(result, arg)
        return result