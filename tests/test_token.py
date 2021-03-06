import unittest
from expression_evaluator.token import *

class TestTokenMethods(unittest.TestCase):

    def test_token_creation(self):
        token = Token(TokenType.Number, 0)
        self.assertIsNotNone(token)

    def test_token_string(self):
        self.assertIsInstance(str(Token(TokenType.Number, 0)), str)