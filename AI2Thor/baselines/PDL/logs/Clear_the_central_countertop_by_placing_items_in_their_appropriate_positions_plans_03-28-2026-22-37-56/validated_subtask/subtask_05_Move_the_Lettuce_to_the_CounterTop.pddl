(define (problem move-lettuce-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    countertop - object
    countertop1 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location lettuce countertop)
    (at-location countertop1 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location lettuce countertop1)
  ))

  (:metric minimize (total-cost))
)