import unittest
from expression_evaluator.expression import *

class BasicExpressionTestMethods(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Expression('1 + 1').evaluate()[0], 1+1)
    
    def test_subtraction(self):
        self.assertEqual(Expression('1 - 1').evaluate()[0], 1-1)

    def test_multiply(self):
        self.assertEqual(Expression('2 * 2').evaluate()[0], 2*2)

    def test_divide(self):
        self.assertEqual(Expression('4 / 2').evaluate()[0], 4/2)

    def test_power_1(self):
        self.assertEqual(Expression('2 ^ 2').evaluate()[0], 2**2)
    
    def test_power_2(self):
        self.assertEqual(Expression('2 ** 2').evaluate()[0], 2**2)

    def test_D(self):
        self.assertNotEqual(Expression('2D6').evaluate(), 0)

    def test_scope_parenthesis(self):
        self.assertEqual(Expression('1 + (2 * 5)').evaluate()[0], 11)

    def test_pi(self):
        self.assertEqual(Expression('PI').evaluate()[0], math.pi)