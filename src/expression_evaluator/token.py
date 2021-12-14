from expression_evaluator.types import *

class Token:
    type = TokenType.Number
    token_id: int = 0
    priority = PriorityLevel.Number
    value: int = 0

    def __init__(self, token_id: int, scope_level, value=0):
        self.token_id = token_id
        self.value = value
        self.priority_level = int(self.priority.value) + (scope_level * 10)

    def __str__(self):
        if self.type == TokenType.Number:
            return str(self.value)
        if self.type == TokenType.BasicOperator or self.type == TokenType.AdvanceOperator or self.type == TokenType.Variable:
            return str(type(self))
        else:
            return 'Invalid Token'

class Operator(Token):
    type = TokenType.INVALID
    is_sign = False
    symbols = []
    priority = PriorityLevel.Operator

    def __init__(self, token_id, scope_level):
        super().__init__(token_id, scope_level)

    @classmethod
    def function(cls, *args):
        return cls._function(*args)

    @classmethod
    def _function(cls, *args):
        raise Exception("Missing _function classmethod in Operator!")

class BasicOperator(Operator):
    type = TokenType.BasicOperator
    priority = PriorityLevel.Operator

class AdvanceOperator(Operator):
    type = TokenType.AdvanceOperator
    priority = PriorityLevel.Operator

class ConstantOperator(Operator):
    type = TokenType.Constant
    priority = PriorityLevel.Number

class VariableOperator(Operator):
    type = TokenType.Variable
    priority = PriorityLevel.Number

    def __init__(self, token_id: int, scope_level: int, variable_name: str):
        super().__init__(token_id, scope_level)
        self.variable_name = variable_name
