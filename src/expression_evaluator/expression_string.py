import re
from expression_evaluator.operators import basic
from expression_evaluator.token import *
from expression_evaluator.operator import *

class ExpressionString:
    def __init__(self, string, string_literal_quotes):
        self.string = string
        self.string_literal_quotes = string_literal_quotes

    def __iter__(self):
        self.index = 0
        self.token_counter = 0
        self.scope_level = 0
        self.parse_flags = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.SIGN
        return self

    def __next__(self):
        # Stop iterating if we have moved past the string
        if self.index >= len(self.string):
            if self.scope_level != 0:
                raise Exception("Unmatched \"()\"")
            raise StopIteration
        
        # Step forward if we are on whitespace
        if self.IsWhitespace():
            self.index += 1
            return self.__next__()
        
        # Check for 
        string = self.GetString()
        if string:
            return self.__next__()

        # Check for numbers
        number = self.GetNumber()
        if not isinstance(number, bool):
            if not (self.parse_flags & ParseFlag.PRIMARY):
                raise Exception("Unexpected Number")
            self.parse_flags = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA
            self.token_counter += 1
            if number.isdecimal():
                return Token(self.token_counter-1, self.scope_level, int(number))
            return Token(self.token_counter-1, self.scope_level, float(number))

        # Check for basic operators first
        basic_operator = self.GetBasicOperator()
        if basic_operator:
            if not (self.parse_flags & ParseFlag.OPERATOR):
                raise Exception('Unexpected Basic Operator')
            self.parse_flags = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.SIGN    
            self.token_counter += 1
            token = basic_operator(self.token_counter-1, self.scope_level)
            return token

        advance_operator = self.GetAdvanceOperator()
        if advance_operator:
            if not (self.parse_flags & ParseFlag.OPERATOR):
                raise Exception('Unexpected Advance Operator')
            self.parse_flags = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.SIGN
            self.token_counter += 1
            token = advance_operator(self.token_counter - 1, self.scope_level)
            return token

        # Check for left parenthesis
        if self.IsLeftParenthesis():
            if not (self.parse_flags & ParseFlag.LPAREN):
                raise Exception("Unexpected \"(\"")
            self.scope_level += 1
            self.index += 1
            self.parse_flags = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.SIGN
            return self.__next__()

        # Check for right parenthesis
        if self.IsRightParenthesis():
            if not (self.parse_flags & ParseFlag.RPAREN):
                raise Exception("Unexpected \")\"")
            self.parse_flags = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA | ParseFlag.LPAREN
            self.scope_level -= 1
            self.index += 1
            return self.__next__()

        # Check for comma
        if self.IsComma():
            if not (self.parse_flags & ParseFlag.COMMA):
                raise Exception("Unexpected \",\"")
            self.index += 1
            return self.__next__()

        # Check for constants
        constant = self.GetConstant()
        if constant: 
            if not (self.parse_flags & ParseFlag.PRIMARY):
                raise Exception("Unexpected Constant")
            self.parse_flags = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA
            self.token_counter += 1
            token = constant(self.token_counter - 1, self.scope_level)
            return token

        variable = self.GetVariable()
        if variable:
            if not (self.parse_flags & ParseFlag.PRIMARY):
                raise Exception("Unexpected Variable")
            self.token_counter += 1
            token = variable(self.token_counter - 1, self.scope_level)
            self.parse_flags = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA | ParseFlag.LPAREN
            return token

        raise Exception('Invalid character! - ' + self.string[self.index])

    def IsWhitespace(self):
        return self.string[self.index] == ' '

    def IsLeftParenthesis(self):
        return self.string[self.index] == '('

    def IsRightParenthesis(self):
        return self.string[self.index] == ')'

    def IsComma(self):
        return self.string[self.index] == ','

    def IsLogicalNot(self):
        return self.string[self.index - 4: self.index] == 'not '

    def GetBasicOperator(self):
        basic_operator = False
        for operator in Operators(TokenType.BasicOperator):
            for symbol in operator.symbols:
                if self.string.startswith(symbol, self.index):
                    self.index += len(symbol)
                    basic_operator = operator
        return basic_operator

    def GetAdvanceOperator(self):
        for operator in Operators(TokenType.AdvanceOperator):
            for symbol in operator.symbols:
                if self.string.startswith(symbol, self.index):
                    self.index += len(symbol)
                    return operator
        return False

    def GetNumber(self):
        # Check for scientific notation numbers
        scientific_notation = re.match(r'([-+]?([0-9]*\.?[0-9]*)[eE][-+]?[0-9]+).*', self.string[self.index:])
        if scientific_notation:
            self.index += len(scientific_notation)
            return scientific_notation.group(1)

        # Check for decimal numbers
        decimal_string = ''
        for character in self.string[self.index:]:
            if (len(decimal_string) == 0 and character == '.'):
                decimal_string = '0.'
            elif (character >= '0' and character <= '9'):
                decimal_string += character
            else:
                break
        
        self.index += len(decimal_string)
        if len(decimal_string) > 0:
            return decimal_string
        return False

    def GetString(self):
        start_index = self.index
        string = ''
        if self.string[self.index] in self.string_literal_quotes:
            quote_type = self.string[self.index]
            self.index += 1

            while self.index < len(self.string):
                current_character = self.string[self.index]
                self.index += 1
                if current_character != quote_type or (string != '' and string[-1] == '\\'):
                    string += current_character
                else:
                    break
        if len(string) > 0:
            return True
        self.index = start_index 
        return False

    def GetConstant(self):
        for operator in Operators(TokenType.Constant):
            for symbol in operator.symbols:
                string = self.string[self.index:self.index+len(symbol)]
                if symbol == string:
                    self.index += len(symbol)
                    return operator
        return False

    def GetVariable(self):
        return False