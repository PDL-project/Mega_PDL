(define (problem place-bread-on-countertop2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    countertop2 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (holding robot1 bread)
    (at-location countertop2 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location bread countertop2)
  ))

  (:metric minimize (total-cost))
)