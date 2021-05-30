from pddlyacc import parser

data = ''' 
    (define
        (domain construction)
        (:requirements :strips :typing)
        (:types
             object
             material
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
                (or
                    (walls-built ?s)
                    (windows-fitted ?s)
                )
                (when
                    (and (has-hot-chocolate ?p ?c) (has-marshmallows ?c))
                    (and (person-is-happy ?p))
                )
                (forall (?c - crane)
                    (crane-is-free ?c)
                )
                (exists (?c - crane)
                    (crane-is-free ?c)
                )
                (not (= ?s1 ?s2))

            )
            :effect (and
                (increase (score s) 199)
                (when
                    (not (= (scared-time g0) 0))
                    (decrease (scared-time g0) 1)
                )

                (walls-built ?s)
                (material-used ?b)
                (when
                    (pill-at ?p2)
                    (and
                        (assign (scared-time g0) 40)
                        (assign (scared-time g1) 40)
                   )
                )


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


domain = parser.parse(data)
print(domain)