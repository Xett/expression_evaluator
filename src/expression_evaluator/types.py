from enum import *

class TokenType(IntEnum):
    INVALID = 0
    Number = 1
    BasicOperator = 2
    AdvanceOperator = 4
    Constant = 8
    Variable = 16

class ParseFlag(IntFlag):
    PRIMARY = 1
    OPERATOR = 2
    LPAREN = 4
    RPAREN = 8
    COMMA = 16
    SIGN = 32

class PriorityLevel(IntEnum):
    Operator = 0
    Roll = 1
    And = 1
    String = 3
    Boolean = 3
    Subtract = 4
    Not = 5
    Sign = 5
    Add = 5
    Multiply = 5
    Divide = 6
    Power = 8
    Number = 9