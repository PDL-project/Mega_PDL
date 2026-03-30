(define (problem drop-bread)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    Bread - object
    countertop2 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 Bread)
    (at-location countertop2 kitchen)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location Bread countertop2)
  ))

  (:metric minimize (total-cost))
)