
from expression_evaluator.types import *
from expression_evaluator.token import Token
from expression_evaluator.parser import Parser

class Expression:

    def __init__(self, tokens):
        self.tokens = tokens

    def simplify(self, values):
        values = values or {}
        nstack = []
        newexpression = []
        L = len(self.tokens)
        for i in range(0, L):
            item = self.tokens[i]
            type_ = item.type_
            if type_ == TokenType.TNUMBER:
                nstack.append(item)
            elif type_ == TokenType.TVAR and item.index_ in values:
                item = Token(TokenType.TNUMBER, 0, 0, values[item.index_])
                nstack.append(item)
            elif type_ == TokenType.TOP2 and len(nstack) > 1:
                n2 = nstack.pop()
                n1 = nstack.pop()
                f = self.ops2[item.index_]
                item = Token(TokenType.TNUMBER, 0, 0, f(n1.number_, n2.number_))
                nstack.append(item)
            elif type_ == TokenType.TOP1 and nstack:
                n1 = nstack.pop()
                f = self.ops1[item.index_]
                item = Token(TokenType.TNUMBER, 0, 0, f(n1.number_))
                nstack.append(item)
            else:
                while len(nstack) > 0:
                    newexpression.append(nstack.pop(0))
                newexpression.append(item)
        while nstack:
            newexpression.append(nstack.pop(0))

        return Expression(newexpression, self.ops1, self.ops2, self.functions)

    def substitute(self, variable, expr):
        if not isinstance(expr, Expression):
            expr = Parser().parse(str(expr))
        newexpression = []
        L = len(self.tokens)
        for i in range(0, L):
            item = self.tokens[i]
            type_ = item.type_
            if type_ == TokenType.TVAR and item.index_ == variable:
                for j in range(0, len(expr.tokens)):
                    expritem = expr.tokens[j]
                    replitem = Token(
                        expritem.type_,
                        expritem.index_,
                        expritem.prio_,
                        expritem.number_,
                    )
                    newexpression.append(replitem)
            else:
                newexpression.append(item)

        ret = Expression(newexpression, self.ops1, self.ops2, self.functions)
        return ret

    def evaluate(self, values):
        values = values or {}
        nstack = []
        L = len(self.tokens)
        for item in self.tokens:
            type_ = item.type_
            if type_ == TokenType.TNUMBER:
                nstack.append(item.number_)
            elif type_ == TokenType.TOP2:
                n2 = nstack.pop()
                n1 = nstack.pop()
                f = self.ops2[item.index_]
                nstack.append(f(n1, n2))
            elif type_ == TokenType.TVAR:
                if item.index_ in values:
                    nstack.append(values[item.index_])
                elif item.index_ in self.functions:
                    nstack.append(self.functions[item.index_])
                else:
                    raise Exception('undefined variable: ' + item.index_)
            elif type_ == TokenType.TOP1:
                n1 = nstack.pop()
                f = self.ops1[item.index_]
                nstack.append(f(n1))
            elif type_ == TokenType.TFUNCALL:
                n1 = nstack.pop()
                f = nstack.pop()
                if callable(f):
                    if type(n1) is list:
                        nstack.append(f(*n1))
                    else:
                        nstack.append(f(n1))
                else:
                    raise Exception(f + ' is not a function')
            else:
                raise Exception('invalid Expression')
        if len(nstack) > 1:
            raise Exception('invalid Expression (parity)')
        return nstack[0]

    def toString(self, toJS=False):
        nstack = []
        L = len(self.tokens)
        for i in range(0, L):
            item = self.tokens[i]
            type_ = item.type_
            if type_ == TokenType.TNUMBER:
                if type(item.number_) == str:
                    nstack.append("'"+item.number_+"'")
                else:
                    nstack.append( item.number_)
            elif type_ == TokenType.TOP2:
                n2 = nstack.pop()
                n1 = nstack.pop()
                f = item.index_
                if toJS and f == '^':
                    nstack.append('math.pow(' + n1 + ',' + n2 + ')')
                else:
                    frm='({n1}{f}{n2})'
                    if f == ',':
                        frm = '{n1}{f}{n2}'

                    nstack.append(frm.format(
                        n1=n1,
                        n2=n2,
                        f=f,
                    ))


            elif type_ == TokenType.TVAR:
                nstack.append(item.index_)
            elif type_ == TokenType.TOP1:
                n1 = nstack.pop()
                f = item.index_
                if f == '-':
                    nstack.append('(' + f + str(n1) + ')')
                else:
                    nstack.append(f + '(' + str(n1) + ')')
            elif type_ == TokenType.TFUNCALL:
                n1 = nstack.pop()
                f = nstack.pop()
                nstack.append(f + '(' + n1 + ')')
            else:
                raise Exception('invalid Expression')
        if len(nstack) > 1:
            raise Exception('invalid Expression (parity)')
        return nstack[0]

    def __str__(self):
        return self.toString()

    def symbols(self):
        vars = []
        for i in range(0, len(self.tokens)):
            item = self.tokens[i]
            if item.type_ == TokenType.TVAR and not item.index_ in vars:
                vars.append(item.index_)
        return vars

    def variables(self):
        return [
            sym for sym in self.symbols()
            if sym not in self.functions]