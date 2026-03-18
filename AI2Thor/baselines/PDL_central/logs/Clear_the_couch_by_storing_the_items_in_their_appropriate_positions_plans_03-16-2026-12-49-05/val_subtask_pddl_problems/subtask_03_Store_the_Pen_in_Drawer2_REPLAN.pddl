(define (problem store-pen-in-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    drawer2 - object
    floor - object
    kitchen - object
    sofa1 - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pen sofa1)
    (at-location drawer2 floor)
    (object-close robot1 drawer2)
    (not (holding robot1 pen))
  )

  (:goal (and
    (at-location pen drawer2)
    (object-close robot1 drawer2)
  ))

  (:metric minimize (total-cost))
)