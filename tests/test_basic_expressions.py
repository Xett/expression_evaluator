import unittest
from expression_evaluator.expression import *

class BasicExpressionTestMethods(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Expression('1 + 1').evaluate(), 1+1)
    
    def test_subtraction(self):
        self.assertEqual(Expression('1 - 1').evaluate(), 1-1)

    def test_multiply(self):
        self.assertEqual(Expression('2 * 2').evaluate(), 2*2)

    def test_divide(self):
        self.assertEqual(Expression('4 / 2').evaluate(), 4/2)

    def test_power_1(self):
        self.assertEqual(Expression('2 ^ 2').evaluate(), 2**2)
    
    def test_power_2(self):
        self.assertEqual(Expression('2 ** 2').evaluate(), 2**2)

    def test_D(self):
        self.assertNotEqual(Expression('2D6').evaluate(), 0)