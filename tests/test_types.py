import unittest
from expression_evaluator.types import *

class TestTypesMethods(unittest.TestCase):

    def test_token_types(self):
        self.assertIsInstance(TokenType.Number, TokenType)
        self.assertIsInstance(TokenType.BasicOperator, TokenType)
        self.assertIsInstance(TokenType.AdvanceOperator, TokenType)
        self.assertIsInstance(TokenType.Variable, TokenType)
        self.assertIsInstance(TokenType.Function, TokenType)
        self.assertIsInstance(TokenType.Constant, TokenType)

    def test_parse_flags(self):
        self.assertIsInstance(ParseFlag.PRIMARY, ParseFlag)
        self.assertIsInstance(ParseFlag.OPERATOR, ParseFlag)
        self.assertIsInstance(ParseFlag.FUNCTION, ParseFlag)
        self.assertIsInstance(ParseFlag.LPAREN, ParseFlag)
        self.assertIsInstance(ParseFlag.RPAREN, ParseFlag)
        self.assertIsInstance(ParseFlag.COMMA, ParseFlag)
        self.assertIsInstance(ParseFlag.SIGN, ParseFlag)
        self.assertIsInstance(ParseFlag.CALL, ParseFlag)
        self.assertIsInstance(ParseFlag.NULLARY_CALL, ParseFlag)