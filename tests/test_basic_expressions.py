import unittest
from expression_evaluator.expression import *

class BasicExpressionTestMethods(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Expression('1 + 1').evaluate(), 2)
        return