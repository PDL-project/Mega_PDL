(define (problem place-vase2-on-countertop2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    vase2 - object
    countertop2 - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (holding robot1 vase2)
    (at robot1 floor)
    (at-location countertop2 floor)
    (not (object-close robot1 countertop2))
  )

  (:goal (and
    (at-location vase2 countertop2)
    (not (holding robot1 vase2))
  ))

  (:metric minimize (total-cost))
)