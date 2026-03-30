(define (problem move-spatula-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spatula - object
    countertop - object
    countertop1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location spatula countertop)
    (at-location countertop1 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location spatula countertop1)
  ))

  (:metric minimize (total-cost))
)