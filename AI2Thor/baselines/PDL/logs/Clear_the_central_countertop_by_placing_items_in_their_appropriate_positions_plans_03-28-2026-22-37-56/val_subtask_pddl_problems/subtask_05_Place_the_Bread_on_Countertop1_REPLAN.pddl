(define (problem place-bread-on-countertop1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    countertop1 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (holding robot1 bread)
    (at-location countertop1 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location bread countertop1)
  ))

  (:metric minimize (total-cost))
)