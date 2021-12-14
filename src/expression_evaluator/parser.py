from expression_evaluator.token import *
from expression_evaluator.operator import *
from expression_evaluator.expression_string import *
from expression_evaluator.token_stack import *

class Parser:

    def __init__(self, string_literal_quotes = ("'", "\"")):
        self.string_literal_quotes = string_literal_quotes

        self.success = False
        self.errormsg = ''

    def parse(self, expression):
        token_stack = TokenStack()

        for token in ExpressionString(expression, self.string_literal_quotes):
            token_stack.add(token)
        
        return token_stack
        
        #while position < len(expression):            
        
        #    if self.isOperator():
        #        if self.isSign() and expected & ParseFlag.SIGN:
        #            if self.isNegativeSign():
        #                self.tokenprio = 5
        #                self.tokenindex = '-'
        #                noperators += 1
        #                self.addfunc(token_stack, operator_stack, TokenType.TOP1)
        #            expected = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN
        #        elif self.isLogicalNot() and expected & ParseFlag.SIGN:
        #            self.tokenprio = 2
        #            self.tokenindex = 'not'
        #            noperators += 1
        #            self.addfunc(token_stack, operator_stack, TokenType.TOP1)
        #            expected = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN
        #        elif self.isComment():
        #            pass
        #        else:
        #            if expected and ParseFlag.OPERATOR == 0:
        #                self.error_parsing(position, 'unexpected operator')
        #            noperators += 2
        #            self.addfunc(token_stack, operator_stack, TokenType.TOP2)
        #            expected = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN
        
        #    elif self.isNumber():
        #        if expected and ParseFlag.PRIMARY == 0:
        #            self.error_parsing(position, 'unexpected number')
        #        token = Token(TokenType.TNUMBER, 0, 0, self.tokennumber)
        #        token_stack.append(token)
        #        expected = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA
        
        #    elif self.isString():
        #        if (expected & ParseFlag.PRIMARY) == 0:
        #            self.error_parsing(position, 'unexpected string')
        #        token = Token(TokenType.TNUMBER, 0, 0, self.tokennumber)
        #        token_stack.append(token)
        #        expected = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA
        
        #    elif self.isLeftParenth():
        #        if (expected & ParseFlag.LPAREN) == 0:
        #            self.error_parsing(position, 'unexpected \"(\"')
        #        if expected & ParseFlag.CALL:
        #            noperators += 2
        #            self.tokenprio = -2
        #            self.tokenindex = -1
        #            self.addfunc(token_stack, operator_stack, TokenType.TFUNCALL)
        #        expected = \
        #            ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | \
        #            ParseFlag.SIGN | ParseFlag.NULLARY_CALL
        
        #    elif self.isRightParenth():
        #        if expected & ParseFlag.NULLARY_CALL:
        #            token = Token(TokenType.TNUMBER, 0, 0, [])
        #            token_stack.append(token)
        #        elif (expected & ParseFlag.RPAREN) == 0:
        #            self.error_parsing(position, 'unexpected \")\"')
        #        expected = \
        #            ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA | \
        #            ParseFlag.LPAREN | ParseFlag.CALL
        
        #    elif self.isComma():
        #        if (expected & ParseFlag.COMMA) == 0:
        #            self.error_parsing(position, 'unexpected \",\"')
        #        self.addfunc(token_stack, operator_stack, TokenType.TOP2)
        #        noperators += 2
        #        expected = \
        #            ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN
        
        #    elif self.isConst():
        #        if (expected & ParseFlag.PRIMARY) == 0:
        #            self.error_parsing(position, 'unexpected constant')
        #        consttoken = Token(TokenType.TNUMBER, 0, 0, self.tokennumber)
        #        token_stack.append(consttoken)
        #        expected = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA
        
        #    elif self.isOp2():
        #        if (expected & ParseFlag.FUNCTION) == 0:
        #            self.error_parsing(position, 'unexpected function')
        #        self.addfunc(token_stack, operator_stack, TokenType.TOP2)
        #        noperators += 2
        #        expected = ParseFlag.LPAREN
        
        #    elif self.isOp1():
        #        if (expected & ParseFlag.FUNCTION) == 0:
        #            self.error_parsing(position, 'unexpected function')
        #        self.addfunc(token_stack, operator_stack, TokenType.TOP1)
        #        noperators += 1
        #        expected = ParseFlag.LPAREN
        
        #    elif self.isVar():
        #        if (expected & ParseFlag.PRIMARY) == 0:
        #            self.error_parsing(position, 'unexpected variable')
        #        vartoken = Token(TokenType.TVAR, self.tokenindex, 0, 0)
        #        token_stack.append(vartoken)
        #        expected = \
        #            ParseFlag.OPERATOR | ParseFlag.RPAREN | \
        #            ParseFlag.COMMA | ParseFlag.LPAREN | ParseFlag.CALL
        
        #    elif self.isWhite():
        #        pass
        
        #    else:
        #        if self.errormsg == '':
        #            self.error_parsing(expression, position, 'unknown character')
        #        else:
        #            self.error_parsing(expression, position, self.errormsg)
        
        #if temp_priority < 0 or temp_priority >= 10:
        #    self.error_parsing(expression, position, 'unmatched \"()\"')
        
        #while len(operator_stack) > 0:
        #    token_stack.append(operator_stack.pop())
        
        #if (noperators + 1) != len(token_stack):
        #    self.error_parsing(expression, position, 'parity')

    #def unescape(self, v, pos):
    #    buffer = []
    #    escaping = False
    #
    #    for i in range(0, len(v)):
    #        c = v[i]
    #
    #        if escaping:
    #            if c == "'":
    #                buffer.append("'")
    #                break
    #            elif c == '\\':
    #                buffer.append('\\')
    #                break
    #            elif c == '/':
    #                buffer.append('/')
    #                break
    #            elif c == 'b':
    #                buffer.append('\b')
    #                break
    #            elif c == 'f':
    #                buffer.append('\f')
    #                break
    #            elif c == 'n':
    #                buffer.append('\n')
    #                break
    #            elif c == 'r':
    #                buffer.append('\r')
    #                break
    #            elif c == 't':
    #                buffer.append('\t')
    #                break
    #            elif c == 'u':
    #                # interpret the following 4 characters
    #                # as the hex of the unicode code point
    #                codePoint = int(v[i + 1, i + 5], 16)
    #                buffer.append(chr(codePoint))
    #                i += 4
    #                break
    #            else:
    #                raise self.error_parsing(
    #                    pos + i,
    #                    'Illegal escape sequence: \'\\' + c + '\'',
    #                )
    #            escaping = False
    #       else:
    #            if c == '\\':
    #                escaping = True
    #            else:
    #                buffer.append(c)
    #
    #    return ''.join(buffer)

    #def isConst(self):
    #    for i in self.consts:
    #        L = len(i)
    #        str = self.expression[self.pos:self.pos+L]
    #        if i == str:
    #            if len(self.expression) <= self.pos + L:
    #                self.tokennumber = self.consts[i]
    #                self.pos += L
    #                return True
    #            if not self.expression[self.pos + L].isalnum() and self.expression[self.pos + L] != "_":
    #                self.tokennumber = self.consts[i]
    #                self.pos += L
    #                return True
    #    return False

    #def isComma(self):
    #    code = self.expression[self.pos]
    #    if code==',':
    #        self.pos+=1
    #        self.tokenprio=-1
    #        self.tokenindex=","
    #        return True
    #    return False

    #def isOp1(self):
    #    str = ''
    #    for i in range(self.pos, len(self.expression)):
    #        c = self.expression[i]
    #        if c.upper() == c.lower():
    #            if i == self.pos or (c != '_' and (c < '0' or c > '9')):
    #                break
    #        str += c
    #    if len(str) > 0 and str in ops1:
    #        self.tokenindex = str
    #        self.tokenprio = 9
    #        self.pos += len(str)
    #        return True
    #    return False

    #def isOp2(self):
    #    str = ''
    #    for i in range(self.pos, len(self.expression)):
    #        c = self.expression[i]
    #        if c.upper() == c.lower():
    #            if i == self.pos or (c != '_' and (c < '0' or c > '9')):
    #                break
    #        str += c
    #    if len(str) > 0 and (str in ops2):
    #        self.tokenindex = str
    #        self.tokenprio = 9
    #        self.pos += len(str)
    #        return True
    #    return False

    #def isVar(self):
    #    str = ''
    #    inQuotes = False
    #    for i in range(self.pos, len(self.expression)):
    #        c = self.expression[i]
    #        if c.lower() == c.upper():
    #            if ((i == self.pos and c != '"') or (not (c in '_."') and (c < '0' or c > '9'))) and not inQuotes :
    #                break
    #        if c == '"':
    #            inQuotes = not inQuotes
    #        str += c
    #    if str:
    #        self.tokenindex = str
    #        self.tokenprio = 6
    #        self.pos += len(str)
    #        return True
    #    return False
