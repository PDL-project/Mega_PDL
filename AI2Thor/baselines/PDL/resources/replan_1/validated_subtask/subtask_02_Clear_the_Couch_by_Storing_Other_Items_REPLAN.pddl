(define (problem clear-couch)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    pencil - object
    sofa1 - object
    armchair1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location pen sofa1)
    (at-location pencil sofa1)

    (not (holding robot1 pen))
    (not (holding robot1 pencil))

    (object-close robot1 armchair1)
  )

  (:goal (and
    (at-location pen armchair1)
    (at-location pencil armchair1)
    (object-close robot1 armchair1)
  ))

  (:metric minimize (total-cost))
)