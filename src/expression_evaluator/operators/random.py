import random
from expression_evaluator.token import *

class Random(Operator):
    type = TokenType.Function | TokenType.Variable
    symbols = ['random']

    @classmethod
    def _function(cls, a):
        return random.random() * (a or 1)