import unittest
from expression_evaluator.types import *

class TestTypesMethods(unittest.TestCase):

    def test_token_types(self):
        self.assertIsInstance(TokenType.TNUMBER, TokenType)
        self.assertIsInstance(TokenType.TOP1, TokenType)
        self.assertIsInstance(TokenType.TOP2, TokenType)
        self.assertIsInstance(TokenType.TVAR, TokenType)
        self.assertIsInstance(TokenType.TFUNCALL, TokenType)

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

    def test_operator_types(self):
        self.assertIsInstance(OperatorType.Basic, OperatorType)
        self.assertIsInstance(OperatorType.Advanced, OperatorType)
        self.assertIsInstance(OperatorType.Function, OperatorType)
        self.assertIsInstance(OperatorType.Constant, OperatorType)
        self.assertIsInstance(OperatorType.Value, OperatorType)