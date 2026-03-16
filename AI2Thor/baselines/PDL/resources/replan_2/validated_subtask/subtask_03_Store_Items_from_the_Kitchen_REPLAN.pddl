(define (problem store-items-from-kitchen)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pencil - object
    kitchen - object
    sofa1 - object
    drawer1 - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 sofa1)
    (at-location pencil sofa1)
    (object-close robot1 drawer1)
  )

  (:goal (and
    (at-location pencil drawer1)
    (object-close robot1 drawer1)
  ))

  (:metric minimize (total-cost))
)