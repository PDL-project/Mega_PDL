(define (problem put-vase2-on-countertop2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    vase2 - object
    shelf2 - object
    countertop2 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location vase2 shelf2)
    (at-location countertop2 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location vase2 countertop2)
  ))

  (:metric minimize (total-cost))
)