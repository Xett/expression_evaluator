from expression_evaluator.token import *

class Add(BasicOperator):
    is_sign = True
    symbols = ['+']
    priority = PriorityLevel.Add

    @classmethod    
    def _function(cls, a, b):
        return a + b