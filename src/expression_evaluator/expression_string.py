import re
from expression_evaluator.token import *
from expression_evaluator.operator import *

class ExpressionString:
    def __init__(self, string: str):
        self.string = string

    def __iter__(self):
        self.index = 0
        self.token_counter = 0
        self.current_parse_flags = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN
        return self

    def __next__(self):
        # Stop iterating if we have moved past the string
        if self.index >= len(self.string):
            raise StopIteration

        while self.IsWhitespace():
            self.index += 1
        
        # Check for basic operators first
        operator = self.GetOperator()
        if operator and TokenType.BasicOperator in operator.type:
            if self.current_parse_flags and ParseFlag.SIGN:
                # Check for - sign
                if operator.is_sign and '-' in operator.symbols:
                        self.current_parse_flags = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN
                
            self.token_counter += 1
            return operator(self.token_counter-1)

        # Check for numbers
        number = self.GetNumber()
        if not isinstance(number, bool):
            self.token_counter += 1
            return Token(self.token_counter-1, number)

        # Check for string

        # Check for left parenthesis

        # Check for right parenthesis

        # Check for comma

        # Check for constants



        raise Exception('Invalid character! - ' + self.string[self.index])

    def IsWhitespace(self):
        return self.string[self.index] == ' '

    def GetOperator(self):
        for operator in Operators().operators:
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