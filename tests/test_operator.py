import unittest
from expression_evaluator import operator

class TestOperatorsMethods(unittest.TestCase):
    fail_messages = [
        "Operators Initialising Failed!",
        "No Operators loaded!"
    ]
    
    def test_creation(self):
        self.assertIsNotNone(operator.Operators(), self.fail_messages[0])

    def test_operators_loaded(self):
        self.assertGreater(len(operator.Operators().operators), 0, self.fail_messages[1])