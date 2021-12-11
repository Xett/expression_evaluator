import re
from expression_evaluator.token import *
from expression_evaluator.operator import *

class ExpressionString:
    def __init__(self, string: str):
        self.string = string

    def __iter__(self):
        self.index = 0
        self.token_counter = 0
        return self

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        
        token = self.GetToken()
        self.index += 1
        return token

    def GetToken(self):
        token_type = self.GetCurrentTokenType()

        if token_type == TokenType.Number:
            token = Token(self.token_counter, self.GetNumber())
            self.token_counter += 1
            return token

        if token_type == TokenType.BasicOperator:
            return

        token_index = 0
        return Token(token_type, token_index)
        raise Exception('Not a valid character!\nNo Token Option found!')

    def GetCurrentTokenType(self):
        # Check for Operators first
        operator = self.GetCurrentOperator()
        if operator:
            return operator.type
        # Check for numbers
        numbers = re.match(r'([-+]?([0-9]*\.?[0-9]*)[eE][-+]?[0-9]+).*', self.string[self.index:])
        if numbers:
            return TokenType.Number
        return None

    def GetCurrentOperator(self):
        for operator in Operators().operators:
            for symbol in operator.symbols:
                if self.string.startswith(symbol, self.index):
                    return operator
        return False
#                token_priority = operator.priority
#                token_index = operator.index
#                self.index += len(operator.token)

    def IsNumber(self):
        return False

    def IsLeftParenthisis(self):
        return

    def IsRightParenthisis(self):
        return

    def GetNumber(self):
        numbers = re.match(r'([-+]?([0-9]*\.?[0-9]*)[eE][-+]?[0-9]+).*', self.string[self.index:])
        if numbers:
            return float(numbers.group(1))