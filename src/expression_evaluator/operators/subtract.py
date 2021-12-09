from .._operator import *

class Subtract(Operator):
    label: str = 'sub'
    description: str = 'subtraction'
    symbol: str = '-'

    def _function(a, b):
        return a - b