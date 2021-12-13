from expression_evaluator.token import *

class Add(BasicOperator):
    is_sign = True
    symbols = ['+']
    priority = 5

    @classmethod    
    def _function(cls, a, b):
        return a + b