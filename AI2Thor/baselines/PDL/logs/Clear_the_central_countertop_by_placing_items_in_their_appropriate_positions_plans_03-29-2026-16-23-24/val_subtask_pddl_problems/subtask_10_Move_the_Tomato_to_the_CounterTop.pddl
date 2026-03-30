(define (problem move-tomato-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tomato - object
    countertop2 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location tomato countertop2)
    (at-location countertop2 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location tomato countertop2)
  ))

  (:metric minimize (total-cost))
)