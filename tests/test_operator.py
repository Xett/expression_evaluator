import unittest
from expression_evaluator import operator
from expression_evaluator.types import *

class TestOperatorsMethods(unittest.TestCase):
    fail_messages = [
        "Operators Initialising Failed!",
        "No Operators loaded!",
        "No Basic Operators!",
        "No Advanced Operators!",
        "No Function Operators!",
        "No Constant Operators!",
        "No Value Operators!"
    ]
    
    def test_creation(self):
        self.assertIsNotNone(operator.Operators(), self.fail_messages[0])

    def test_operators_loaded(self):
        self.assertGreater(len(operator.Operators().operators), 0, self.fail_messages[1])

    def test_basic_operators_loaded(self):
        self.assertGreater(len(operator.Operators().GetTypes(TokenType.BasicOperator)), 0, self.fail_messages[2])

    def test_advanced_operators_loaded(self):
        self.assertGreater(len(operator.Operators().GetTypes(TokenType.AdvanceOperator)), 0, self.fail_messages[3])

    def test_function_operators_loaded(self):
        self.assertGreater(len(operator.Operators().GetTypes(TokenType.Function)), 0, self.fail_messages[4])
    
    def test_constant_operators_loaded(self):
        self.assertGreater(len(operator.Operators().GetTypes(TokenType.Constant)), 0, self.fail_messages[5])
    
    def test_value_operators_loaded(self):
        self.assertGreater(len(operator.Operators().GetTypes(TokenType.Variable)), 0, self.fail_messages[6])

    def test_add_operator_exists(self):
        self.assertIsNotNone(operator.Operators().Get('+'))

    def test_subtract_operator_loaded(self):
        self.assertIsNotNone(operator.Operators().Get('-'))

    def test_multiply_operator_loaded(self):
        self.assertIsNotNone(operator.Operators().Get('*'))

    def test_divide_operator_loaded(self):
        self.assertIsNotNone(operator.Operators().Get('/'))

    def test_modulo_operator_loaded(self):
        self.assertIsNotNone(operator.Operators().Get('%'))

    def test_power_operator_loaded(self):
        self.assertIsNotNone(operator.Operators().Get('**'))
        self.assertIsNotNone(operator.Operators().Get('^'))

    def test_equal_operator_loaded(self):
        self.assertIsNotNone(operator.Operators().Get('=='))

    def test_greater_than_operator_loaded(self):
        self.assertIsNotNone(operator.Operators().Get('>'))

    def test_lesser_than_operator_loaded(self):
        self.assertIsNotNone(operator.Operators().Get('<'))

    def test_greater_than_equal_operator_loaded(self):
        self.assertIsNotNone(operator.Operators().Get('>='))

    def test_lesser_than_equal_operator_loaded(self):
        self.assertIsNotNone(operator.Operators().Get('<='))