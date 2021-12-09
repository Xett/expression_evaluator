from expression_evaluator.types import *

class NotOperator(Operator):
    label: str = 'notOperator'
    description: str = 'not operator'
    symbols: list = ['not']
    type: OperatorType = OperatorType.Advanced

    def _function(a):
        return not a