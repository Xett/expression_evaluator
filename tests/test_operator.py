import unittest
from expression_evaluator import _operator

class TestOperatorsMethods(unittest.TestCase):
    fail_messages = [
        "Operators Initialising Failed!",
        "No Operators loaded!"
    ]
    def test_creation(self):
        self.assertIsNotNone(_operator.Operators(), self.fail_messages[0])

    def test_operators_leaded(self):
        self.assertGreater(len(_operator.Operators().operators), 0, self.fail_messages[1])