import unittest
import unittest.mock
from expression_evaluator.token import *

class TokenStackTestMethods(unittest.TestCase):

    def test_token_stack_creation(self):
        self.assertIsNotNone(TokenStack())

    def test_token_stack(self):
        token_1 = Token(0, 0)
        token_2 = Token(1, 0)
        token_stack = TokenStack()
        token_stack.add(token_1)
        token_stack.add(token_2)

        self.assertEqual(len(token_stack), 2)
        self.assertEqual(len(token_stack.stack[9]), 2)

        token_3 = Token(2, 0)
        token_3.priority_level = 1
        token_stack.add(token_3)

        self.assertEqual(len(token_stack), 3)
        self.assertEqual(len(token_stack.stack[9]), 2)
        self.assertEqual(len(token_stack.stack[1]), 1)

    def test_token_stack_iteration(self):
        token_1 = Token(0, 0)
        token_2 = Token(1, 0)
        token_3 = Token(2, 0)

        token_3.priority_level = 1

        token_stack = TokenStack()
        token_stack.add(token_1)
        token_stack.add(token_2)
        token_stack.add(token_3)

    def test_priority_order(self):
        token_1 = Token(0, 0)

        token_stack = TokenStack()
        token_stack.add(token_1)

        self.assertEqual(token_stack.priority_order(), [9])
        
        token_2 = Token(0, 0)
        token_2.priority_level = 1
        token_stack.add(token_2)

        self.assertEqual(token_stack.priority_order(), [9, 1])

    def test_current_priority(self):
        token_1 = Token(0, 0)
        
        token_stack = TokenStack()
        token_stack.add(token_1)

        token_stack.current_priority = unittest.mock.MagicMock()

        self.assertIsNotNone(token_stack.current_priority())

    def test_iteration(self):
        token_stack = TokenStack()
        
        token_1 = Token(0, 0)
        token_stack.add(token_1)

        self.assertEqual(len(token_stack), 1)
    
        for token in token_stack:
            self.assertIsNotNone(token)