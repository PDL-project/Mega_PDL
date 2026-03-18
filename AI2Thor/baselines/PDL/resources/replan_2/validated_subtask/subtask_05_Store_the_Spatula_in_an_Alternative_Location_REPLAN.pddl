(define (problem store-spatula)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spatula - object
    cabinet1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 spatula)
    (object-close robot1 cabinet1)
  )

  (:goal (and
    (at-location spatula cabinet1)
    (object-close robot1 cabinet1)
  ))

  (:metric minimize (total-cost))
)