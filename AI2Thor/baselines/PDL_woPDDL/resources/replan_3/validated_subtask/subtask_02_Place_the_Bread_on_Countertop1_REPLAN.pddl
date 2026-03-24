(define (problem place-bread-in-cabinet1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    cabinet1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 bread)
    (at-location cabinet1 kitchen)
    (object-open robot1 cabinet1)
  )

  (:goal (and
    (at-location bread cabinet1)
    (object-close robot1 cabinet1)
  ))

  (:metric minimize (total-cost))
)