(define (problem place-pen-and-pick-pencil)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    pencil - object
    drawer2 - object
    sofa1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (holding robot1 pen)
    (at-location pencil sofa1)

    (object-close robot1 drawer2)
  )

  (:goal (and
    (at-location pen drawer2)
    (object-close robot1 drawer2)
    (holding robot1 pencil)
  ))

  (:metric minimize (total-cost))
)