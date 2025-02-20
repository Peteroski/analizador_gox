#En este archivo se definen dos clases

from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    
    #PALABRAS RESERVADAS
    TRUE = "true"
    FALSE = "false"
    CONST = "const"
    VAR = "var"
    PRINT = "print"
    RETURN = "return"
    BREAK = "break"
    CONTINUE = "continue"
    IF = "if"
    ELSE = "else"
    WHILE = "while"
    FUNC = "func"
    IMPORT = "import"
    
    #SIMBOLOS MISELANEOS
    ASSIGN = '='           
    SEMI = ';'
    LPAREN = '('
    RPAREN = ')'
    LBRACE = '{'
    RBRACE = '}'
    COMMA = ','
    DEREF = '`'
    
    #OPERADORES
    PLUS = '+'
    MINUS = '-'
    TIMES = '*'
    DIVIDE = '/'
    LT = '<'
    LE = '<='
    GT = '>'
    GE = '>='
    EQ = '=='
    NE = '!='
    LAND = '&&'
    LOR = '||'
    GROW = '^'
    
    def __str__(self) -> str:
        return self.name
    
@dataclass
class Token:
    token_type: TokenType
    lexeme: str

    def __repr__(self) -> str:
        return f'{self.token_type}("{self.lexeme}")'
    
    