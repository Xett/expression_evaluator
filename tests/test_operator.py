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
        self.assertGreater(len(operator.Operators().GetTypes(OperatorType.Basic)), 0, self.fail_messages[2])

    def test_advanced_operators_loaded(self):
        self.assertGreater(len(operator.Operators().GetTypes(OperatorType.Advanced)), 0, self.fail_messages[3])

    def test_function_operators_loaded(self):
        self.assertGreater(len(operator.Operators().GetTypes(OperatorType.Function)), 0, self.fail_messages[4])
    
    def test_constant_operators_loaded(self):
        self.assertGreater(len(operator.Operators().GetTypes(OperatorType.Constant)), 0, self.fail_messages[5])
    
    def test_value_operators_loaded(self):
        self.assertGreater(len(operator.Operators().GetTypes(OperatorType.Value)), 0, self.fail_messages[6])