from .._operator import *

class Add(Operator):
    label: str = 'add'
    description: str = 'addition'
    symbol: str = '+'

    def _function(a, b):
        return a + b