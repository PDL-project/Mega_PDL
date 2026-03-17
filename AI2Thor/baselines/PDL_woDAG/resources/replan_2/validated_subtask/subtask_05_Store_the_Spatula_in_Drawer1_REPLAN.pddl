(define (problem store-spatula-in-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spatula - object
    drawer2 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 spatula)
    (at-location drawer2 kitchen)
    (object-close robot1 drawer2)
  )

  (:goal (and
    (at-location spatula drawer2)
    (object-close robot1 drawer2)
  ))

  (:metric minimize (total-cost))
)