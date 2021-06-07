(define (problem pb0)
    (:domain pacman)
    (:objects
              p00 p01 p02 p03 p04 - pos
              g0 g1 - ghost
              s - score
    )
    (:init
            (= (score s) 0)
            (= (scared-time g0) 0)
            (= (scared-time g1) 0)
            (at p03 g0)
            (pac-at p00)
            (food-at p01)
            (food-at p04)
            (pill-at p02)
            (adj p00 p01)
            (adj p01 p02)
            (adj p02 p03)
            (adj p03 p04)
    )
    (:goal
        (forall ( ?p - pos)
          (not (food-at ?p))
        )
    )
    (:metric maximize (score s))
)