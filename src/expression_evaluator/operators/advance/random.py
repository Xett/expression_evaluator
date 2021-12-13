import random
from expression_evaluator.token import *

class Random(AdvanceOperator):
    symbols = ['random']

    @classmethod
    def _function(cls, a):
        return random.random() * (a or 1)