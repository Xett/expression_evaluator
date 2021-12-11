import random
from expression_evaluator.token import *

class Random(Operator):
    type: TokenType = TokenType.Function | TokenType.Variable
    symbols: list = ['random']

    def _function(a):
        return random.random() * (a or 1)