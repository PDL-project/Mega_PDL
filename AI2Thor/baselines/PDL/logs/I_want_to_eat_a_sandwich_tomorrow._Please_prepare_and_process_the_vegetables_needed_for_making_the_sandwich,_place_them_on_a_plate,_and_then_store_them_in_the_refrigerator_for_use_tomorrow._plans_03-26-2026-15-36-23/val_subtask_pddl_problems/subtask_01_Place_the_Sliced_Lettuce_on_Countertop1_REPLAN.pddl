(define (problem place-sliced-lettuce-on-countertop1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    countertop1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 lettuce)
    (holding robot1 lettuce)
    (at-location countertop1 kitchen)
  )

  (:goal (and
    (at-location lettuce countertop1)
    (not (holding robot1 lettuce))
  ))

  (:metric minimize (total-cost))
)