from .._operator import *

class Multiply(Operator):
    label: str = 'mul'
    description: str = 'multiply'
    symbol: str = '*'


    def _function(a, b):
        return a * b