(define (problem drop-bread-on-floor)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (holding robot1 bread)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location bread floor)
  ))

  (:metric minimize (total-cost))
)