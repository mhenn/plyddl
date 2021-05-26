from ply import lex


tokens = (
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'EXTENDS',
    'DEFINE',
    'DOMAIN'
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_EQUALS = r'\='
t_EXTENDS = r'\:extends'
t_DEFINE = r'define'
t_DOMAIN = r'domain'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\.+'
    t.value = str(t.value)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

data = ''' 
       (define 
       (domain )
       )
       '''

lexer = lex.lex()
lexer.input(data)

while True:
     tok = lexer.token()
     if not tok:
         break      # No more input
     print(tok)