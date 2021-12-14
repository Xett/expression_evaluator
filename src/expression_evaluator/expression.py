from expression_evaluator.types import *
from expression_evaluator.token import *
from expression_evaluator.parser import *
from expression_evaluator.operator import *

class Expression:

    def __init__(self, string: str, **kwargs):
        self.string = string
        self.values = kwargs
        self.token_stack = Parser(self.values).parse(string)

    def __iter__(self):
        return self.token_stack

    def evaluate(self):
        evaluation_stack = []
        for token in self:
            if token.type == TokenType.Number:
                evaluation_stack.append(token.value)
            elif token.type == TokenType.BasicOperator:
                n2 = evaluation_stack.pop()
                n1 = evaluation_stack.pop()
                evaluation_stack.append(token.function(n1, n2))
            elif token.type == TokenType.Variable:
                if token.variable_name in self.values.keys():
                    evaluation_stack.append(self.values[token.variable_name])
            elif token.type == TokenType.AdvanceOperator:
                n1 = evaluation_stack.pop()
                evaluation_stack.append(token.function(n1))
            elif token.type == TokenType.Constant:
                evaluation_stack.append(token.function())
            else:
                raise Exception("Invalid Expression!")
        return evaluation_stack