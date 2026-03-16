(define (problem clear-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    pencil - object
    sofa1 - object
    drawer1 - object
    drawer2 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location pen sofa1)
    (at-location pencil sofa1)
    (at-location sofa1 floor)

    (object-close robot1 drawer1)
    (object-close robot1 drawer2)

    (not (holding robot1 pen))
    (not (holding robot1 pencil))
  )

  (:goal (and
    (at-location pen drawer1)
    (at-location pencil drawer2)
    (object-close robot1 drawer1)
    (object-close robot1 drawer2)
  ))

  (:metric minimize (total-cost))
)