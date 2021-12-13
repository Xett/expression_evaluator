from enum import Enum, IntFlag

class CharacterType(Enum):
    String = 0
    Number = 1
    Constant = 2
    Operator = 3
    Whitespace = 4
    Comma = 5
    LeftParenthesis = 6
    RightParenthesis = 7

class TokenType(IntFlag):
    INVALID = 0
    Number = 1
    BasicOperator = 2
    AdvanceOperator = 4
    Constant = 8
    Variable = 16

class ParseFlag(IntFlag):
    PRIMARY = 1
    OPERATOR = 2
    FUNCTION = 4
    LPAREN = 8
    RPAREN = 16
    COMMA = 32
    SIGN = 64
    CALL_START = 128
    CALL_END = 256

#ops1 = {
#    'sin': math.sin,
#    'cos': math.cos,
#    'tan': math.tan,
#    'asin': math.asin,
#    'acos': math.acos,
#    'atan': math.atan,
#
#    'sind': sind,
#    'cosd': cosd,
#    'tand': tand,
#    'asind': asind,
#    'acosd': acosd,
#    'atand': atand,
#
#    'sqrt': math.sqrt,
#    'abs': abs,
#    'ceil': math.ceil,
#    'floor': math.floor,
#    'round': round,
#    '-': neg,
#    'not': notOperator,
#    'exp': math.exp,
#}

#ops2 = {
#    '+': add,
#    '-': sub,
#    '*': mul,
#    '/': div,
#    '%': mod,
#    '^': pow,
#    '**': pow,
#    ',': append,
#    '||': concat,
#    "==": equal,
#    "!=": notEqual,
#    ">": greaterThan,
#    "<": lessThan,
#    ">=": greaterThanEqual,
#    "<=": lessThanEqual,
#    "and": andOperator,
#    "or": orOperator,
#    "xor": xorOperator,
#    "in": inOperator,
#    "D": roll
#}

#functions = {
#    'random': random,
#    'fac': fac,
#    'log': math.log,
#    'min': min,
#    'max': max,
#    'pyt': pyt,
#    'pow': math.pow,
#    'atan2': math.atan2,
#    'concat':concat,
#    'if': ifFunction
#}

#consts = {
#    'E': math.e,
#    'PI': math.pi,
#}

#values = {
#    'sin': math.sin,
#    'cos': math.cos,
#    'tan': math.tan,
#    'asin': math.asin,
#    'acos': math.acos,
#    'atan': math.atan,
#    'sqrt': math.sqrt,
#    'log': math.log,
#    'abs': abs,
#    'ceil': math.ceil,
#    'floor': math.floor,
#    'round': round,
#    'random': random,
#    'fac': fac,
#    'exp': math.exp,
#    'min': min,
#    'max': max,
#    'pyt': pyt,
#    'pow': math.pow,
#    'atan2': math.atan2,
#    'E': math.e,
#    'PI': math.pi
#}