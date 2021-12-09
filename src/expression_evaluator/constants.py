from enum import Enum, IntFlag
import math

from .__ops import *

class TokenType(Enum):
    TNUMBER = 0
    TOP1 = 1
    TOP2 = 2
    TVAR = 3
    TFUNCALL = 4

class ParseFlag(IntFlag):
    PRIMARY = 1
    OPERATOR = 2
    FUNCTION = 4
    LPAREN = 8
    RPAREN = 16
    COMMA = 32
    SIGN = 64
    CALL = 128
    NULLARY_CALL = 256

ops1 = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'asin': math.asin,
    'acos': math.acos,
    'atan': math.atan,

    'sind': sind,
    'cosd': cosd,
    'tand': tand,
    'asind': asind,
    'acosd': acosd,
    'atand': atand,

    'sqrt': math.sqrt,
    'abs': abs,
    'ceil': math.ceil,
    'floor': math.floor,
    'round': round,
    '-': neg,
    'not': notOperator,
    'exp': math.exp,
}

ops2 = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '%': mod,
    '^': pow,
    '**': pow,
    ',': append,
    '||': concat,
    "==": equal,
    "!=": notEqual,
    ">": greaterThan,
    "<": lessThan,
    ">=": greaterThanEqual,
    "<=": lessThanEqual,
    "and": andOperator,
    "or": orOperator,
    "xor": xorOperator,
    "in": inOperator,
    "D": roll
}

functions = {
    'random': random,
    'fac': fac,
    'log': math.log,
    'min': min,
    'max': max,
    'pyt': pyt,
    'pow': math.pow,
    'atan2': math.atan2,
    'concat':concat,
    'if': ifFunction
}

consts = {
    'E': math.e,
    'PI': math.pi,
}

values = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'asin': math.asin,
    'acos': math.acos,
    'atan': math.atan,
    'sqrt': math.sqrt,
    'log': math.log,
    'abs': abs,
    'ceil': math.ceil,
    'floor': math.floor,
    'round': round,
    'random': random,
    'fac': fac,
    'exp': math.exp,
    'min': min,
    'max': max,
    'pyt': pyt,
    'pow': math.pow,
    'atan2': math.atan2,
    'E': math.e,
    'PI': math.pi
}