from expression_evaluator.types import *
from expression_evaluator.operators import *

class Operators:
    class _Operators:
        def __init__(self):
            self.operators = Operator.__subclasses__()

        def Get(self, index):
            return self.operators[index]

        def GetTypes(self, operator_type):
            types = []
            for operator in self.operators:
                if operator_type in operator.type:
                    types.append(operator)
            return types
    
    instance = None

    def __init__(self, value=None):
        if not Operators.instance:
            Operators.instance = Operators._Operators()
        if value is not None:
            return self.instance.Get(value).function

    def __getattr__(self, name):
        return getattr(self.instance, name)