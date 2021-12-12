from expression_evaluator.types import *
from expression_evaluator.operators import *

class Operators:
    class _Operators:
        def __init__(self):
            self.operators = Operator.__subclasses__()
            self.type = TokenType.BasicOperator | TokenType.AdvanceOperator | TokenType.Constant | TokenType.Variable | TokenType.Function
            self.index = 0

        def Get(self, symbol):
            for operator in self.operators:
                if symbol in operator.symbols:
                    return operator
            return None

        def __len__(self):
            if len(self.operators) == 0:
                return 0
            operators = 0
            for operator in self.operators:
                if operator.type and self.type:
                    operators += 1
            return operators

        def __iter__(self):
            self.index = 0
            return self

        def __next__(self):
            if self.index >= len(self.operators):
                raise StopIteration

            self.index += 1
            if self.type and self.operators[self.index - 1].type:
                return self.operators[self.index - 1]
            return self.__next__()
    
    instance = None

    def __init__(self, type=-1):
        if not Operators.instance:
            Operators.instance = Operators._Operators()

        if type == -1:
            Operators.instance.type = TokenType.BasicOperator | TokenType.AdvanceOperator | TokenType.Constant | TokenType.Variable | TokenType.Function
        else:
            Operators.instance.type = type

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __iter__(self):
        return Operators.instance.__iter__()

    def __len__(self):
        return len(Operators.instance)