from pddllex import lexer
from pddlyacc import parser

data = ''' 
    (define
        (domain construction)
        (:requirements :strips :typing)
        (:types
            site material - object
            bricks cables windows - material
        )
        (:predicates 
            (walls-built ?s - site)
            (windows-fitted ?s - site)
            (foundations-set ?s - site)
            (cables-installed ?s - site)
            (site-built ?s - site)
            (on-site ?m - material ?s - site)
            (material-used ?m - material)
        )
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
    )
           '''
#
#lexer.input(data)
#while True:
#    tok = lexer.token()
#    if not tok:
#        break  # No more input
#    print(tok)
#

pb = '''(define
    (problem buildingahouse)
    (:domain construction)
    ;(:situation <situation_name>) ;deprecated
    (:objects 
        s1 - site 
        b - bricks 
        w - windows 
        c - cables
    )
    (:init
        (on-site b s1)
        (on-site c s1)
        (on-site w s1)
    )
    (:goal (and
            (walls-built ?s1)
            (cables-installed ?s1)
            (windows-fitted ?s1)
        )
    )
)
'''


print(parser.parse(pb))