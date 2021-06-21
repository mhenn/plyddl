( define ( domain pacman)
    ( :requirements
        :adl
        :fluents
        :conditional-effects
    )
    ( :types
        ghost
        pos
        score
    )
    (:predicates
        ( food-at  ?p  - pos)
        ( pill-at  ?p  - pos)
        ( pac-at   ?p  - pos)
        ( at ?p - pos ?g - ghost)
        ( adj ?p1 ?p2  - pos)
    )
    (:functions
        (scared-time ?g - ghost)
        (score ?s - score)
    )
    ( :action move
        :parameters (?p1 ?p2 - pos )
        :precondition
            ( and
                ;(not (= ?p1 ?p2))
                (adj ?p1 ?p2)
                (pac-at ?p1)
                (forall (?g - ghost)
                    (not (at ?p2 ?g))
                )
            )
        :effect
        ( and

            (when
                (not (= (scared-time g0) 0))
                (decrease (scared-time g0) 1)
            )
            (when
                (not (= (scared-time g1) 0))
                (decrease (scared-time g1) 1)
            )

            (when
                (pill-at ?p2)
                (and
                    (assign (scared-time g0) 40)
                    (assign (scared-time g1) 40)
                )
            )
            (when
                (food-at ?p2)
                (increase (score s) 10)
            )
            (pac-at ?p2 )
            (not (pac-at ?p1))
            (not (food-at ?p2))
            (not (pill-at ?p2))
        )
    )
    (:action eat-ghost
        :parameters (?p1 ?p2 - pos ?g - ghost)
        :precondition
            (and
                ;(not (= ?p1 ?p2))
                (adj ?p1 ?p2)
                (pac-at ?p1)
                (at ?p2 ?g)
                ( > (scared-time ?g) 0)
            )
        :effect
            (and
                (increase (score s) 199)
                (when
                    (not (= (scared-time g0) 0))
                    (decrease (scared-time g0) 1)
                )
                (when
                    (not (= (scared-time g1) 0))
                    (decrease (scared-time g1) 1)
                )
                (assign (scared-time ?g) 0)
                (when
                    (pill-at ?p2)
                    (and
                        (assign (scared-time g0) 40)
                        (assign (scared-time g1) 40)
                   )
                )

                (pac-at ?p2 )
                (not (pac-at ?p1))
                (not (food-at ?p2))
                (not (pill-at ?p2))
            )
    )
)
