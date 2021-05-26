from pddllex import lexer
from pddlyacc import parser

data = ''' 
           (define
           (domain construction)
           )
           '''
print(parser.parse(data))