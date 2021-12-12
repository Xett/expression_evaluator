import re
from expression_evaluator.token import *
from expression_evaluator.operator import *

class ExpressionString:
    def __init__(self, string: str):
        self.string = string

    def __iter__(self):
        self.index = 0
        self.token_counter = 0
        self.parse_flags = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN
        return self

    def __next__(self):
        # Stop iterating if we have moved past the string
        if self.index >= len(self.string):
            raise StopIteration

        initial_index = self.index
        # Check for basic operators first
        operator = self.GetOperator()
        if operator:
            print(operator.type)
            # If we are expection a sign (+/-)
            # We only need to check for -
            if self.parse_flags and ParseFlag.SIGN > 0:
                # Check for - sign
                if operator.is_sign and '-' in operator.symbols:
                        # Set the parse flags
                        self.parse_flags = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN
                        self.token_counter += 1
                        token = operator(self.token_counter - 1)
                        token.priority = 5
                        return token
            self.token_counter += 1
            return operator(self.token_counter-1)

        # Check for numbers
        number = self.GetNumber()
        if not isinstance(number, bool):
            if self.parse_flags and ParseFlag.PRIMARY == 0:
                raise Exception("Unexpected Number")
            self.token_counter += 1
            self.parse_flags = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA
            return Token(self.token_counter-1, number)

        # Check for 
        string = self.GetString()
        if string:
            if self.parse_flags and ParseFlag.PRIMARY == 0:
                raise Exception("Unexpected String")

        # Check for left parenthesis
        while self.IsLeftParenthesis():
            if self.parse_flags and ParseFlag.LPAREN == 0:
                raise Exception("Unexpected \"(\"")
            elif self.parse_flags and ParseFlag.CALL:
                self.parse_flags = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN | ParseFlag.NULLARY_CALL

                self.index += 1

        # Check for right parenthesis
        while self.IsRightParenthesis():
            if self.parse_flags and ParseFlag.RPAREN == 0:
                raise Exception("Unexpected \")\"")

        # Check for comma
        while self.IsComma():
            if self.parse_flags and ParseFlag.COMMA == 0:
                raise Exception("Unexpected \",\"")

        # Check for constants
        constant = self.GetConstant()
        if constant: 
            if self.parse_flags and ParseFlag.PRIMARY == 0:
                raise Exception("Unexpected Constant")
            self.parse_flags = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA
            self.token_counter += 1
            return Token(self.token_counter - 1, operator.function())

        variable = self.GetVariable()
        if variable: # Use get instead
            if self.parse_flags and ParseFlag.PRIMARY == 0:
                raise Exception("Unexpected Variable")

        
        # Step forward while we are on whitespace
        if self.IsWhitespace():
            self.index += 1

        if initial_index != self.index:
            return self.__next__()
        
        raise Exception('Invalid character! - ' + self.string[self.index])

    def IsWhitespace(self):
        return self.string[self.index] == ' '

    def IsLeftParenthesis(self):
        return self.string[self.index] == '('

    def IsRightParenthesis(self):
        return self.string[self.index] == ')'

    def IsComma(self):
        return self.string[self.index] == ','

    def GetOperator(self):
        for operator in Operators(TokenType.BasicOperator):
            for symbol in operator.symbols:
                if self.string.startswith(symbol, self.index):
                    self.index += len(symbol)
                    return operator
        return False

    def GetNumber(self):
        # Check for scientific notation numbers
        scientific_notation = re.match(r'([-+]?([0-9]*\.?[0-9]*)[eE][-+]?[0-9]+).*', self.string[self.index:])
        number = False
        if scientific_notation:
            number = float(scientific_notation.group(1))
            self.index += len(scientific_notation)
            return number

        # Check for decimal numbers
        decimal_string = ''
        for character in self.string[self.index:]:
            if (len(decimal_string) == 0 and character == '.'):
                decimal_string = '0.'
            elif (character >= '0' and character <= '9'):
                decimal_string += character
            else:
                break
        try:
            number = int(decimal_string)
            self.index += len(decimal_string)
            return number
        except ValueError:
            try:
                number = float(decimal_string)
                self.index += len(decimal_string)
                return number
            except ValueError:
                return False

    def GetString(self):
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