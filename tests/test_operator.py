import unittest
from expression_evaluator import operator
from expression_evaluator.operator import *
from expression_evaluator.types import *
import math

class TestOperatorsMethods(unittest.TestCase):
    fail_messages = [
        "Operators Initialising Failed!",
        "No Operators loaded!",
        "Unexpected number of Basic Operators!",
        "Unexpected number of Advanced Operators!",
        "Unexpected number of Function Operators!",
        "Unexpected number of Constant Operators!",
        "Unexpected number of Variable Operators!"
    ]
    
    def test_creation(self):
        self.assertIsNotNone(Operators(), self.fail_messages[0])

    def test_operators_loaded(self):
        self.assertGreater(len(Operators()), 0, self.fail_messages[1])

    def test_basic_operators_loaded(self):
        self.assertEqual(len(Operators(TokenType.BasicOperator)), 20, self.fail_messages[2])

    def test_advanced_operators_loaded(self):
        self.assertEqual(len(Operators(TokenType.AdvanceOperator)), 28, self.fail_messages[3])
    
    def test_constant_operators_loaded(self):
        self.assertEqual(len(Operators(TokenType.Constant)), 2, self.fail_messages[5])
    
    def test_value_operators_loaded(self):
        self.assertEqual(len(Operators(TokenType.Variable)), 0, self.fail_messages[6])

    def test_add_operator_exists(self):
        operator = Operators().Get('+')
        self.assertIsNotNone(operator)
        self.assertEqual(operator, Add)

    def test_subtract_operator_loaded(self):
        operator = Operators().Get('-')
        self.assertIsNotNone(operator)
        self.assertEqual(operator, Subtract)

    def test_multiply_operator_loaded(self):
        operator = Operators().Get('*')
        self.assertIsNotNone(operator)
        self.assertEqual(operator, Multiply)

    def test_divide_operator_loaded(self):
        operator = Operators().Get('/')
        self.assertIsNotNone(operator, Divide)

    def test_modulo_operator_loaded(self):
        operator = Operators().Get('%')
        self.assertIsNotNone(operator)
        self.assertEqual(operator, Modulo)

    def test_power_operator_loaded(self):
        operator1 = Operators().Get('**')
        operator2= Operators().Get('^')
        self.assertIsNotNone(operator1)
        self.assertEqual(operator1, Power)
        self.assertIsNotNone(operator2)
        self.assertEqual(operator2, Power)

    def test_equal_operator_loaded(self):
        operator = Operators().Get('==')
        self.assertIsNotNone(operator)
        self.assertEqual(operator, Equal)

    def test_greater_than_operator_loaded(self):
        operator = Operators().Get('>')
        self.assertIsNotNone(operator)
        self.assertEqual(operator, GreaterThan)

    def test_lesser_than_operator_loaded(self):
        operator = Operators().Get('<')
        self.assertIsNotNone(operator)
        self.assertEqual(operator, LesserThan)

    def test_greater_than_equal_operator_loaded(self):
        operator = Operators().Get('>=')
        self.assertIsNotNone(operator)
        self.assertEqual(operator, GreaterThanEqual)

    def test_lesser_than_equal_operator_loaded(self):
        operator = Operators().Get('<=')
        self.assertIsNotNone(operator)
        self.assertEqual(operator, LesserThanEqual)

    def test_pi_operator_loaded(self):
        operator = Operators().Get('PI')
        self.assertIsNotNone(operator)
        self.assertEqual(operator, PIOperator)
        self.assertEqual(operator.function(), math.pi)


    def test_roll_operator_loaded(self):
        operator = Operators().Get('D')
        self.assertIsNotNone(operator)
        self.assertEqual(operator, RollOperator)