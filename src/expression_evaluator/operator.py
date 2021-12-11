from expression_evaluator.types import *
from expression_evaluator.operators import *

class Operators:
    class _Operators:
        def __init__(self):
            self.operators = Operator.__subclasses__()

        def Get(self, symbol):
            for operator in self.operators:
                if symbol in operator.symbols:
                    return operator
            return None

        def GetTypes(self, operator_type):
            types = []
            for operator in self.operators:
                if operator_type in operator.type:
                    types.append(operator)
            return types
    
    instance = None

    def __init__(self):
        if not Operators.instance:
            Operators.instance = Operators._Operators()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        raise StopIteration