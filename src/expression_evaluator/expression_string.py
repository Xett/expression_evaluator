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
        self.parse_flags = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN
        return self

    def __next__(self):
        # Stop iterating if we have moved past the string
        if self.index >= len(self.string):
            if self.scope_level != 0:
                raise Exception("Unmatched \"()\"")
            raise StopIteration
        
        # Check for basic operators first
        basic_operator = self.GetBasicOperator()
        if basic_operator:
            # If we are expection a sign (+/-)
            # We only need to check for -
            if self.parse_flags & ParseFlag.SIGN:
                # Check for - sign
                if basic_operator.is_sign and '-' in basic_operator.symbols:
                    # Set the parse flags
                    self.parse_flags = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN
                    self.token_counter += 1
                    token = basic_operator(self.token_counter - 1, self.scope_level)
                    return token
            self.parse_flags = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN

            # elif is logical not         
            self.token_counter += 1
            token = basic_operator(self.token_counter-1, self.scope_level)
            return token

        advance_operator = self.GetAdvanceOperator()
        if advance_operator:
            if not (self.parse_flags & ParseFlag.FUNCTION):
                return

        # Check for numbers
        number = self.GetNumber()
        if not isinstance(number, bool):
            if not (self.parse_flags & ParseFlag.PRIMARY):
                raise Exception("Unexpected Number")
            self.token_counter += 1
            self.parse_flags = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA
            int_num = 0
            float_num = 0.0
            try:
                int_num = int(number)
            except:
                try:
                    float_num = float(number)
                except:
                    pass
                else:
                    token = Token(self.token_counter-1, self.scope_level, float_num)
                    return token
            else:
                token = Token(self.token_counter-1, self.scope_level, int_num)
                return token

        # Check for 
        string = self.GetString()
        if string:
            if not (self.parse_flags & ParseFlag.PRIMARY):
                raise Exception("Unexpected String")

        # Check for left parenthesis
        if self.IsLeftParenthesis():
            if not (self.parse_flags & ParseFlag.LPAREN):
                raise Exception("Unexpected \"(\"")
            elif self.parse_flags & ParseFlag.CALL_START:
                self.parse_flags = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN | ParseFlag.CALL_END
            self.scope_level += 1
            self.index += 1
            self.parse_flags = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN | ParseFlag.CALL_END
            return self.__next__()

        # Check for right parenthesis
        if self.IsRightParenthesis():
            if not (self.parse_flags & ParseFlag.RPAREN):
                raise Exception("Unexpected \")\"")
            elif self.parse_flags & ParseFlag.CALL_END:
                self.token_counter += 1
                self.scope_level -= 1
                self.index += 1
                token = Token(self.token_counter - 1, self.scope_level)
                self.parse_flags = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA | ParseFlag.LPAREN | ParseFlag.CALL_START
                return token
            self.parse_flags = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA | ParseFlag.LPAREN | ParseFlag.CALL_START
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
            token = Token(self.token_counter - 1, self.scope_level, constant.function())
            token.priority += self.scope_level * 10
            return token

        variable = self.GetVariable()
        if variable:
            if not (self.parse_flags & ParseFlag.PRIMARY):
                raise Exception("Unexpected Variable")
            token = Token()
            self.parse_flags = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA | ParseFlag.LPAREN | ParseFlag.CALL_START
            return token

        # Step forward if we are on whitespace
        if self.IsWhitespace():
            self.index += 1
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
        number = False
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
        #if self.string[self.index] in self.string_literal_quotes:
        #    quote_type = self.string[self.index]
        #    self.index += 1
        #    while self.index < len(self.string):
        #        current_character = self.string[self.index]
        #        if current_character != quote_type or (string != '' and string[-1] == '\\'):
        #            string += self.string[self.index]
        #            self.index += 1
        #        else:
        #            self.index += 1
        #            # token number? value?
        #            return string
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