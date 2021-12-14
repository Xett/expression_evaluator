from expression_evaluator.types import *
from expression_evaluator.operators import *

class Operators:
    class _Operators:
        def __init__(self):
            self.operators = BasicOperator.__subclasses__() + AdvanceOperator.__subclasses__() + ConstantOperator.__subclasses__()
            self.index = 0

        def Get(self, symbol):
            for operator in self.operators:
                for _symbol in operator.symbols:
                    if symbol == _symbol:
                        return operator
            return None

        def GetByType(self, type):
            operators = []
            for operator in self.operators:
                if operator.type == type:
                    operators.append(operator)
            return sorted(operators, key=lambda x : x.priority, reverse=True)

        def __len__(self):
            return len(self.operators)

        def __iter__(self):
            self.index = 0
            return self

        def __next__(self):
            if self.index >= len(self.operators):
                raise StopIteration

            self.index += 1
            return sorted(self.operators, key=lambda x : x.priority, reverse=True)[self.index - 1]
    
    instance = None

    def __new__(cls, type=-1):
        if type == -1 or not Operators.instance:
            return super(Operators, cls).__new__(cls)
        else:
            return Operators.instance.GetByType(type)

    def __init__(self, type=-1):
        if not Operators.instance:
            Operators.instance = Operators._Operators()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __iter__(self):
        return Operators.instance.__iter__()

    def __len__(self):
        return len(Operators.instance)