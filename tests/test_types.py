import unittest
from expression_evaluator.types import *

class TestTypesMethods(unittest.TestCase):

    def test_token_types(self):
        self.assertIsInstance(TokenType.Number, TokenType)
        self.assertIsInstance(TokenType.BasicOperator, TokenType)
        self.assertIsInstance(TokenType.AdvanceOperator, TokenType)
        self.assertIsInstance(TokenType.Variable, TokenType)
        self.assertIsInstance(TokenType.Constant, TokenType)

    def test_parse_flags(self):
        self.assertIsInstance(ParseFlag.PRIMARY, ParseFlag)
        self.assertIsInstance(ParseFlag.OPERATOR, ParseFlag)
        self.assertIsInstance(ParseFlag.LPAREN, ParseFlag)
        self.assertIsInstance(ParseFlag.RPAREN, ParseFlag)
        self.assertIsInstance(ParseFlag.COMMA, ParseFlag)
        self.assertIsInstance(ParseFlag.AdvancedOperator, ParseFlag)

    def test_priority_level(self):
        self.assertIsInstance(PriorityLevel.Operator, PriorityLevel)
        self.assertIsInstance(PriorityLevel.Roll, PriorityLevel)
        self.assertIsInstance(PriorityLevel.And, PriorityLevel)
        self.assertIsInstance(PriorityLevel.String, PriorityLevel)
        self.assertIsInstance(PriorityLevel.Boolean, PriorityLevel)
        self.assertIsInstance(PriorityLevel.Subtract, PriorityLevel)
        self.assertIsInstance(PriorityLevel.Add, PriorityLevel)
        self.assertIsInstance(PriorityLevel.Multiply, PriorityLevel)
        self.assertIsInstance(PriorityLevel.Divide, PriorityLevel)
        self.assertIsInstance(PriorityLevel.Power, PriorityLevel)
        self.assertIsInstance(PriorityLevel.Number, PriorityLevel)