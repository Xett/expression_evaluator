from expression_evaluator.types import *
from dataclasses import dataclass

class Token:
    type = TokenType.Number
    token_id: int = 0
    priority = 9
    value: int = 0

    def __init__(self, token_id: int, scope_level, value=0):
        self.token_id = token_id
        self.value = value
        self.priority += scope_level * 10

    def __str__(self):
        if self.type & TokenType.Number:
            return str(self.value)
        if self.type & (TokenType.BasicOperator | TokenType.AdvanceOperator | TokenType.Variable):
            return str(type(self))
        else:
            return 'Invalid Token'

class Operator(Token):
    type = TokenType.INVALID
    is_sign = False
    symbols = []

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
    priority = 5

class AdvanceOperator(Operator):
    type = TokenType.AdvanceOperator
    priority = 5

class ConstantOperator(Operator):
    type = TokenType.Constant

class VariableOperator(Operator):
    type = TokenType.Variable

class TokenStack:
    def __init__(self):
        self.stack = {}
        self.index = 0
        self.priority_index = 0

    def __len__(self):
        length = 0
        for key in self.stack:
            length += len(self.stack[key])
        return length

    def __iter__(self):
        self.index = 0
        self.priority_index = 0
        return self
        
    def __next__(self):
        current_priority = self.current_priority()
        if current_priority is None:
            raise StopIteration
        elif (self.index >= len(current_priority)) and (self.priority_index >= len(self.priority_order())):
            raise StopIteration

        elif self.index >= len(current_priority):
            self.index = 0
            self.priority_index += 1
            current_priority = self.current_priority()
            if current_priority is None:
                raise StopIteration
        
        if self.index < len(current_priority):
            token = current_priority[self.index]
            self.index += 1
            return token

    def priority_order(self):
        return sorted(self.stack.keys(), reverse=True)

    def current_priority(self):
        if self.priority_index >= len(self.priority_order()):
            return None
        priority_level = self.priority_order()[self.priority_index]
        return self.stack[priority_level]

    def add(self, token):
        if token.priority not in self.stack.keys():
            self.stack[token.priority] = []
        self.stack[token.priority].append(token)
