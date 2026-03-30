(define (problem move-peppershaker-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    peppershaker - object
    countertop - object
    countertop1 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location peppershaker countertop)
    (at-location countertop1 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location peppershaker countertop1)
  ))

  (:metric minimize (total-cost))
)