from expression_evaluator.types import *
from dataclasses import dataclass

class Token:
    type: TokenType = TokenType.Number
    token_id: int = 0
    priority: int = 0
    value: int = 0

    def __init__(self, token_id: int, value=0):
        self.token_id = token_id
        self.value = value

    def __str__(self):
        if self.type == TokenType.Number:
            return str(self.value)
        if self.type == TokenType.BasicOperator or self.type == TokenType.Variable:
            return str(self.token_id)
        elif self.type == TokenType.Function:
            return 'CALL'
        else:
            return 'Invalid Token'

@dataclass(repr=True, eq=True, order=True, frozen=True)
class Operator(Token):
    type: TokenType = TokenType.BasicOperator
    is_sign: bool = False
    symbols = []

    @property
    def function(self):
        return self._function

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
