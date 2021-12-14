from enum import Enum, IntFlag, IntEnum

class TokenType(Enum):
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

class PriorityLevel(IntEnum):
    Operator = 0
    Roll = 1
    And = 1
    String = 3
    Boolean = 3
    Subtract = 4
    Add = 5
    Multiply = 5
    Divide = 6
    Power = 8
    Number = 9