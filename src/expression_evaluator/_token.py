from .constants import *

class Token:
    def __init__(self, token_type: TokenType, index: int, priority: int, number: int):
        self.type = token_type
        self.index = index or 0
        self.priority = priority or 0
        self.number = number if number != None else 0

    def __str__(self):
        if self.type == TokenType.TNUMBER:
            return str(self.number)
        if self.type == TokenType.TOP1 or self.type == TokenType.TOP2 or self.type == TokenType.TVAR:
            return str(self.index)
        elif self.type == TokenType.TFUNCALL:
            return 'CALL'
        else:
            return 'Invalid Token'