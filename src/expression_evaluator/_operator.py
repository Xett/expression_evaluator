from enum import IntFlag
from dataclasses import dataclass
import importlib

class OperatorType(IntFlag):
    Basic = 1
    Advanced = 2
    Function = 4
    Constant = 8
    Value = 16

@dataclass(repr=True, eq=True, order=True, frozen=True)
class Operator:
    type: OperatorType = OperatorType.Basic

    @property
    def function(self):
        return self._function

    def __init__(self):
        return

class Operators:
    class _Operators:
        def __init__(self):
            self.operators = {}
            self.LoadOperators()

        def LoadOperators(self):
            operators_module = importlib.import_module('.operators', package="expression_evaluator")
            classes=dict([(name, cls) for name, cls in operators_module.__dict__.items() if isinstance(cls, type)])
            for name, cls in classes:
                self.operators[cls.symbol] = cls()

        def Get(self, name):
            return self.operators[name]
    
    instance = None

    def __init__(self, value=None):
        if not Operators.instance:
            Operators.instance = Operators._Operators()
        if value is not None:
            return self.instance.Get(value).function

    def __getattr__(self, name):
        return getattr(self.instance, name)