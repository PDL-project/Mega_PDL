(define (problem store-pencil)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pencil - object
    sofa - object
    sidetable3 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pencil sofa)
    (at-location sidetable3 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location pencil sidetable3)
  ))

  (:metric minimize (total-cost))
)