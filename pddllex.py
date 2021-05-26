from ply import lex


tokens = (
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'NAME',
    'VARIABLE',
    'COMMENT'
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = ' \t'
t_EQUALS = r'='

reserved = {
 'define'       :   'DEFINE',
 'domain'       :   'DOMAIN',
 ':extends'     :   'EXTENDS',
 ':requirements':   'REQS',
 ':strips'      :   'REQ_STRIPS',
 ':typing'      :   'REQ_TYPING',
 ':types'       :   'TYPES',
 ':constants'   :   'CONST',
 ':predicates'  :   'PREDICATES',
 ':timeless'    :   'TIMELESS',
 ':action'      :   'ACTION',
 ':parameters'  :   'ACT_PARAM',
 ':precondition':   'ACT_PRE',
 ':effect'      :   'ACT_EFF',
 ':axiom'       :   'AXIOM',
 ':vars'        :   'AXIOM_VARS',
 ':context'     :   'AXIOM_CONTEXT',
 ':implies'     :   'AXIOM_IMPLIES',
 'and'          :   'AND',
 'not'          :   'NOT'
}

tokens += tuple(reserved.values())

def t_KEYWORD(t):
    r':?[a-zA-z_][a-zA-Z_0-9\-]*'
    t.type = reserved.get(t.value, "NAME")
    return t

def t_VARIABLE(t):
    r'\?[a-zA-Z_][a-zA-Z_0-9\-]*'
    t.value = str(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r';.*'

def t_error(t):
    print("Illegal character '%s'" % t.value)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


lexer = lex.lex()
if __name__ == '__main__':
    data = ''' 
           (define
        (domain construction)
        (:extends building)
        (:requirements :strips :typing)
        (:types
            site material - object
            bricks cables windows - material
        )
        (:constants mainsite - site)

        ;(:domain-variables ) ;deprecated

        (:predicates
            (walls-built ?s - site)
            (windows-fitted ?s - site)
            (foundations-set ?s - site)
            (cables-installed ?s - site)
            (site-built ?s - site)
            (on-site ?m - material ?s - site)
            (material-used ?m - material)
        )

        (:timeless (foundations-set mainsite))

        ;(:safety
            ;(forall
            ;    (?s - site) (walls-built ?s)))
            ;deprecated

        (:action BUILD-WALL
            :parameters (?s - site ?b - bricks)
            :precondition (and
                (on-site ?b ?s)
                (foundations-set ?s)
                (not (walls-built ?s))
                (not (material-used ?b))
            )
            :effect (and
                (walls-built ?s)
                (material-used ?b)
            )
            ; :expansion ;deprecated
        )

        (:axiom
            :vars (?s - site)
            :context (and
                (walls-built ?s)
                (windows-fitted ?s)
                (cables-installed ?s)
            )
            :implies (site-built ?s)
        )

        ;Actions omitted for brevity
    )

           '''

    lexer.input(data)
    while True:
         tok = lexer.token()
         if not tok:
             break      # No more input
         print(tok)