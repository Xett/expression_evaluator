import unittest
from expression_evaluator.parser import Parser


class TestParserMethod(unittest.TestCase):
    fail_messages = []

    def parse(self, expression, expected_number_of_tokens):
        token_stack = Parser().parse(expression)
        self.assertIsNotNone(token_stack)
        self.assertEqual(len(token_stack), expected_number_of_tokens)


    def test_parser_creation(self):
        self.assertIsNotNone(Parser())

    def test_parser_addition(self):
        self.parse("1 + 1", 3)

    def test_parser_subtract(self):
        self.parse("1 - 1", 3)

    def test_parser_multiplication(self):
        self.parse("1 * 1", 3)