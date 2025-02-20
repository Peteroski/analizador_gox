from tokens import Token, TokenType

class Scanner:
    def __init__(self, text) -> None:
        self.it = iter(text)
        self.curr = None
        self.advance()
        
    def advance(self):
        try:
            self.curr = next(self.it)
        except StopIteration:
            self.curr = None
    
    #true or false
    #TRUE("true")
    
    def scan(self):
        while self.curr is not None:
            print(self.curr)
            if self.curr.isspace():
                self.advance()
            elif self.curr == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(')
            elif self.curr == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')')
            elif self.curr == '{':
                self.advance()
                return Token(TokenType.LBRACE, '{')
            elif self.curr == '}':
                self.advance()
                return Token(TokenType.RBRACE, '}')
            elif self.curr == '+':
                self.advance()
                return Token(TokenType.PLUS, '+')
            elif self.curr == '-':
                self.advance()
                return Token(TokenType.MINUS, '-')
            elif self.curr == '*':
                self.advance()
                return Token(TokenType.TIMES, '*')
            elif self.curr == '/':
                self.advance()
                return Token(TokenType.DIVIDE, '/')
            elif self.curr == 't':
                self.verify('true')
                return Token(TokenType.TRUE, 'true')
            elif self.curr == '<':
                self.advance()
                if self.curr == '=':
                    return Token(TokenType.LE, '<=')
                else:
                    return Token(TokenType.LT, '<')
            elif self.curr == '>':
                self.advance()
                if self.curr == '=':
                    return Token(TokenType.GE, '>=')
                else:
                    return Token(TokenType.GT, '>')
            elif self.curr == '=':
                self.advance()
                if self.curr == '=':
                    return Token(TokenType.EQ, '==')
                else:
                    return Token(TokenType.ASSIGN, '=')
            elif self.curr == ';':
                self.advance()
                return Token(TokenType.SEMI, ';')
            elif self.curr == ',':
                self.advance()
                return Token(TokenType.COMMA, ',')
            elif self.curr == '`':
                self.advance()
                return Token(TokenType.DEREF, '`')
            elif self.curr == '!':
                self.advance()
                if self.curr == '=':
                    self.advance()
                    return Token(TokenType.NE, '!=')
                else:
                    raise Exception(f'Caracter no valido')
            elif self.curr == '&':
                self.advance()
                if self.curr == '&':
                    self.advance()
                    return Token(TokenType.LAND, '&&')
                else:
                    raise Exception(f'Caracter no valido')
            elif self.curr == '|':
                self.advance()
                if self.curr == '|':
                    self.advance()
                    return Token(TokenType.LOR, '||')
                else:
                    raise Exception(f'Caracter no valido')
            elif self.curr == '^':
                self.advance()
                return Token(TokenType.GROW, '^')

            #IDENTIFICADOR PALABRAS RESERVADAS
            # elif self.curr.isalpha():
            #     identifier = self.curr
            #     self.advance()
            #     while self.curr is not None and (self.curr.isalnum() or self.curr == '_'):
            #         identifier += self.curr
            #         self.advance()
            #     return Token(TokenType.IDENTIFIER, identifier)
            
            #VERIFICAMOS PALABRAS RESERVADAS
            # if identifier == 'const':
            #     return Token(TokenType.CONST, 'identifier')
            # if identifier == 'var':
            #     return Token(TokenType.VAR, 'identifier')
            # if identifier == 'print':
            #     return Token(TokenType.PRINT, 'identifier')
            # if identifier == 'return':
            #     return Token(TokenType.RETURN, 'identifier')
            # if identifier == 'break':
            #     return Token(TokenType.BREAK, 'identifier')
            # if identifier == 'continue':
            #     return Token(TokenType.CONTINUE, 'identifier')
            # if identifier == 'if':
            #     return Token(TokenType.IF, 'identifier')
            # if identifier == 'else':
            #     return Token(TokenType.ELSE, 'identifier')
            # if identifier == 'while':
            #     return Token(TokenType.WHILE, 'identifier')
            # if identifier == 'func':
            #     return Token(TokenType.FUNC, 'identifier')
            # if identifier == 'import':
            #     return Token(TokenType.IMPORT, 'identifier')
            # if identifier == 'true':
            #     return Token(TokenType.TRUE, 'identifier')
            
            # if identifier == 'false':
            #     return Token(TokenType.FALSE, 'identifier')
            else:
                self.advance()
                return f'Caracter ilegal {self.curr!r}'
        return None
    
    def scanAll(self):
        tokens = []
        while True:
            token = self.scan()
            if token is None:
                break
            tokens.append(token)
        return tokens
    
    def verify(self, text):
        for c in text:
            if self.curr is None:
                raise Exception('Token not recognized')
            if self.curr != c:
                raise Exception('Token not recognized')
            self.advance()