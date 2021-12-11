import unittest
from expression_evaluator.parser import Parser


class TestParserMethod(unittest.TestCase):
    fail_messages = []

    def test_parser_creation(self):
        self.assertIsNotNone(Parser())

    def test_parser_addition(self):
        self.assertIsNotNone(Parser().parse("1 + 1"))