(define (problem place-bread-in-cabinet3)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    cabinet3 - object
    kitchen - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 bread)
    (at-location cabinet3 floor)
    (object-close robot1 cabinet3)
  )

  (:goal (and
    (at-location bread cabinet3)
    (object-close robot1 cabinet3)
  ))

  (:metric minimize (total-cost))
)