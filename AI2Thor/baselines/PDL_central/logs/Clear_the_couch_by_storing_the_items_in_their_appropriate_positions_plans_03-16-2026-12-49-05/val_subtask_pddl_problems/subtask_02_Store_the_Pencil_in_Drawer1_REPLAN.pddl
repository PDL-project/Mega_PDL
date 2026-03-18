(define (problem store-pencil-in-drawer1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pencil - object
    drawer1 - object
    sofa - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 sofa)
    (at-location pencil sofa)
    (at-location drawer1 floor)
    (object-close robot1 drawer1)
  )

  (:goal (and
    (at-location pencil drawer1)
    (object-close robot1 drawer1)
    (not (holding robot1 pencil))
  ))

  (:metric minimize (total-cost))
)