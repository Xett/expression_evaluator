#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import re

from expression_evaluator.token import *

class Expression:
    def __init__(self):
        pass


class Parser:

    class Expression(Expression):
        pass

    def __init__(self, string_literal_quotes = ("'", "\"")):
        self.string_literal_quotes = string_literal_quotes

        self.success = False
        self.errormsg = ''
        self.expression = ''

        self.pos = 0

        self.tokennumber = 0
        self.tokenprio = 0
        self.tokenindex = 0
        self.tmpprio = 0

    def parse(self, expr):
        self.errormsg = ''
        self.success = True
        operstack = []
        tokenstack = []
        self.tmpprio = 0
        expected = ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN
        noperators = 0
        self.expression = expr
        self.pos = 0

        while self.pos < len(self.expression):
            if self.isOperator():
                if self.isSign() and expected & ParseFlag.SIGN:
                    if self.isNegativeSign():
                        self.tokenprio = 5
                        self.tokenindex = '-'
                        noperators += 1
                        self.addfunc(tokenstack, operstack, TokenType.TOP1)
                    expected = \
                        ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN
                elif self.isLogicalNot() and expected & ParseFlag.SIGN:
                    self.tokenprio = 2
                    self.tokenindex = 'not'
                    noperators += 1
                    self.addfunc(tokenstack, operstack, TokenType.TOP1)
                    expected = \
                        ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN
                elif self.isComment():
                    pass
                else:
                    if expected and ParseFlag.OPERATOR == 0:
                        self.error_parsing(self.pos, 'unexpected operator')
                    noperators += 2
                    self.addfunc(tokenstack, operstack, TokenType.TOP2)
                    expected = \
                        ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN
            elif self.isNumber():
                if expected and ParseFlag.PRIMARY == 0:
                    self.error_parsing(self.pos, 'unexpected number')
                token = Token(TokenType.TNUMBER, 0, 0, self.tokennumber)
                tokenstack.append(token)
                expected = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA
            elif self.isString():
                if (expected & ParseFlag.PRIMARY) == 0:
                    self.error_parsing(self.pos, 'unexpected string')
                token = Token(TokenType.TNUMBER, 0, 0, self.tokennumber)
                tokenstack.append(token)
                expected = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA
            elif self.isLeftParenth():
                if (expected & ParseFlag.LPAREN) == 0:
                    self.error_parsing(self.pos, 'unexpected \"(\"')
                if expected & ParseFlag.CALL:
                    noperators += 2
                    self.tokenprio = -2
                    self.tokenindex = -1
                    self.addfunc(tokenstack, operstack, TokenType.TFUNCALL)
                expected = \
                    ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | \
                    ParseFlag.SIGN | ParseFlag.NULLARY_CALL
            elif self.isRightParenth():
                if expected & ParseFlag.NULLARY_CALL:
                    token = Token(TokenType.TNUMBER, 0, 0, [])
                    tokenstack.append(token)
                elif (expected & ParseFlag.RPAREN) == 0:
                    self.error_parsing(self.pos, 'unexpected \")\"')
                expected = \
                    ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA | \
                    ParseFlag.LPAREN | ParseFlag.CALL
            elif self.isComma():
                if (expected & ParseFlag.COMMA) == 0:
                    self.error_parsing(self.pos, 'unexpected \",\"')
                self.addfunc(tokenstack, operstack, TokenType.TOP2)
                noperators += 2
                expected = \
                    ParseFlag.PRIMARY | ParseFlag.LPAREN | ParseFlag.FUNCTION | ParseFlag.SIGN
            elif self.isConst():
                if (expected & ParseFlag.PRIMARY) == 0:
                    self.error_parsing(self.pos, 'unexpected constant')
                consttoken = Token(TokenType.TNUMBER, 0, 0, self.tokennumber)
                tokenstack.append(consttoken)
                expected = ParseFlag.OPERATOR | ParseFlag.RPAREN | ParseFlag.COMMA
            elif self.isOp2():
                if (expected & ParseFlag.FUNCTION) == 0:
                    self.error_parsing(self.pos, 'unexpected function')
                self.addfunc(tokenstack, operstack, TokenType.TOP2)
                noperators += 2
                expected = ParseFlag.LPAREN
            elif self.isOp1():
                if (expected & ParseFlag.FUNCTION) == 0:
                    self.error_parsing(self.pos, 'unexpected function')
                self.addfunc(tokenstack, operstack, TokenType.TOP1)
                noperators += 1
                expected = ParseFlag.LPAREN
            elif self.isVar():
                if (expected & ParseFlag.PRIMARY) == 0:
                    self.error_parsing(self.pos, 'unexpected variable')
                vartoken = Token(TokenType.TVAR, self.tokenindex, 0, 0)
                tokenstack.append(vartoken)
                expected = \
                    ParseFlag.OPERATOR | ParseFlag.RPAREN | \
                    ParseFlag.COMMA | ParseFlag.LPAREN | ParseFlag.CALL
            elif self.isWhite():
                pass
            else:
                if self.errormsg == '':
                    self.error_parsing(self.pos, 'unknown character')
                else:
                    self.error_parsing(self.pos, self.errormsg)
        if self.tmpprio < 0 or self.tmpprio >= 10:
            self.error_parsing(self.pos, 'unmatched \"()\"')
        while len(operstack) > 0:
            tmp = operstack.pop()
            tokenstack.append(tmp)
        if (noperators + 1) != len(tokenstack):
            self.error_parsing(self.pos, 'parity')

        return Expression(tokenstack, ops1, ops2, functions)

    def evaluate(self, expr, variables):
        return self.parse(expr).evaluate(variables)

    def error_parsing(self, column, msg):
        self.success = False
        self.errormsg = 'parse error [column ' + str(column) + ']: ' + msg + ', expression: ' + self.expression
        raise Exception(self.errormsg)

    def addfunc(self, tokenstack, operstack, type_):
        operator = Token(
            type_,
            self.tokenindex,
            self.tokenprio + self.tmpprio,
            0,
        )
        while len(operstack) > 0:
            if operator.prio_ <= operstack[len(operstack) - 1].prio_:
                tokenstack.append(operstack.pop())
            else:
                break
        operstack.append(operator)

    def isNumber(self):
        r = False

        if self.expression[self.pos] == 'E':
            return False

        # number in scientific notation
        pattern = r'([-+]?([0-9]*\.?[0-9]*)[eE][-+]?[0-9]+).*'
        match = re.match(pattern, self.expression[self.pos: ])
        if match:
            self.pos += len(match.group(1))
            self.tokennumber = float(match.group(1))
            return True

        # number in decimal
        str = ''
        while self.pos < len(self.expression):
            code = self.expression[self.pos]
            if (code >= '0' and code <= '9') or code == '.':
                if (len(str) == 0 and code == '.' ):
                    str = '0'
                str += code
                self.pos += 1
                try:
                    self.tokennumber = int(str)
                except ValueError:
                    self.tokennumber = float(str)
                r = True
            else:
                break
        return r

    def unescape(self, v, pos):
        buffer = []
        escaping = False

        for i in range(0, len(v)):
            c = v[i]

            if escaping:
                if c == "'":
                    buffer.append("'")
                    break
                elif c == '\\':
                    buffer.append('\\')
                    break
                elif c == '/':
                    buffer.append('/')
                    break
                elif c == 'b':
                    buffer.append('\b')
                    break
                elif c == 'f':
                    buffer.append('\f')
                    break
                elif c == 'n':
                    buffer.append('\n')
                    break
                elif c == 'r':
                    buffer.append('\r')
                    break
                elif c == 't':
                    buffer.append('\t')
                    break
                elif c == 'u':
                    # interpret the following 4 characters
                    # as the hex of the unicode code point
                    codePoint = int(v[i + 1, i + 5], 16)
                    buffer.append(chr(codePoint))
                    i += 4
                    break
                else:
                    raise self.error_parsing(
                        pos + i,
                        'Illegal escape sequence: \'\\' + c + '\'',
                    )
                escaping = False
            else:
                if c == '\\':
                    escaping = True
                else:
                    buffer.append(c)

        return ''.join(buffer)

    def isString(self):
        r = False
        str = ''
        startpos = self.pos
        if self.pos < len(self.expression) and self.expression[self.pos] in self.string_literal_quotes:
            quote_type = self.expression[self.pos]
            self.pos += 1
            while self.pos < len(self.expression):
                code = self.expression[self.pos]
                if code != quote_type or (str != '' and str[-1] == '\\'):
                    str += self.expression[self.pos]
                    self.pos += 1
                else:
                    self.pos += 1
                    self.tokennumber = self.unescape(str, startpos)
                    r = True
                    break
        return r

    def isConst(self):
        for i in self.consts:
            L = len(i)
            str = self.expression[self.pos:self.pos+L]
            if i == str:
                if len(self.expression) <= self.pos + L:
                    self.tokennumber = self.consts[i]
                    self.pos += L
                    return True
                if not self.expression[self.pos + L].isalnum() and self.expression[self.pos + L] != "_":
                    self.tokennumber = self.consts[i]
                    self.pos += L
                    return True
        return False

    def isOperator(self):
        ops = (
            ('**', 8, '**'),
            ('^', 8, '^'),
            ('%', 6, '%'),
            ('/', 6, '/'),
            (u'\u2219', 5, '*'), # bullet operator
            (u'\u2022', 5, '*'), # black small circle
            ('*', 5, '*'),
            ('+', 4, '+'),
            ('-', 4, '-'),
            ('||', 3, '||'),
            ('==', 3, '=='),
            ('!=', 3, '!='),
            ('<=', 3, '<='),
            ('>=', 3, '>='),
            ('<', 3, '<'),
            ('>', 3, '>'),
            ('in ', 3, 'in'),
            ('not ', 2, 'not'),
            ('and ', 1, 'and'),
            ('xor ', 0, 'xor'),
            ('or ', 0, 'or'),
        )
        for token, priority, index in ops:
            if self.expression.startswith(token, self.pos):
                self.tokenprio = priority
                self.tokenindex = index
                self.pos += len(token)
                return True
        return False

    def isSign(self):
        code = self.expression[self.pos - 1]
        return (code == '+') or (code == '-')

    def isPositiveSign(self):
        code = self.expression[self.pos - 1]
        return code == '+'

    def isNegativeSign(self):
        code = self.expression[self.pos - 1]
        return code == '-'

    def isLogicalNot(self):
        code = self.expression[self.pos - 4: self.pos]
        return code == 'not '

    def isLeftParenth(self):
        code = self.expression[self.pos]
        if code == '(':
            self.pos += 1
            self.tmpprio += 10
            return True
        return False

    def isRightParenth(self):
        code = self.expression[self.pos]
        if code == ')':
            self.pos += 1
            self.tmpprio -= 10
            return True
        return False

    def isComma(self):
        code = self.expression[self.pos]
        if code==',':
            self.pos+=1
            self.tokenprio=-1
            self.tokenindex=","
            return True
        return False

    def isWhite(self):
        code = self.expression[self.pos]
        if code.isspace():
            self.pos += 1
            return True
        return False

    def isOp1(self):
        str = ''
        for i in range(self.pos, len(self.expression)):
            c = self.expression[i]
            if c.upper() == c.lower():
                if i == self.pos or (c != '_' and (c < '0' or c > '9')):
                    break
            str += c
        if len(str) > 0 and str in ops1:
            self.tokenindex = str
            self.tokenprio = 9
            self.pos += len(str)
            return True
        return False

    def isOp2(self):
        str = ''
        for i in range(self.pos, len(self.expression)):
            c = self.expression[i]
            if c.upper() == c.lower():
                if i == self.pos or (c != '_' and (c < '0' or c > '9')):
                    break
            str += c
        if len(str) > 0 and (str in self.ops2):
            self.tokenindex = str
            self.tokenprio = 9
            self.pos += len(str)
            return True
        return False

    def isVar(self):
        str = ''
        inQuotes = False
        for i in range(self.pos, len(self.expression)):
            c = self.expression[i]
            if c.lower() == c.upper():
                if ((i == self.pos and c != '"') or (not (c in '_."') and (c < '0' or c > '9'))) and not inQuotes :
                    break
            if c == '"':
                inQuotes = not inQuotes
            str += c
        if str:
            self.tokenindex = str
            self.tokenprio = 6
            self.pos += len(str)
            return True
        return False

    def isComment(self):
        code = self.expression[self.pos - 1]
        if code == '/' and self.expression[self.pos] == '*':
            self.pos = self.expression.index('*/', self.pos) + 2
            if self.pos == 1:
                self.pos = len(self.expression)
            return True
        return False
