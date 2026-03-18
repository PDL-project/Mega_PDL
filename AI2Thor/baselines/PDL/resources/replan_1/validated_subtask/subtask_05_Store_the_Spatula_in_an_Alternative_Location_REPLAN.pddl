(define (problem store-spatula)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spatula - object
    drawer1 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 drawer1)
    (holding robot1 spatula)
    (object-close robot1 drawer1)
  )

  (:goal (and
    (at-location spatula drawer1)
    (object-close robot1 drawer1)
  ))

  (:metric minimize (total-cost))
)