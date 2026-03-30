(define (problem store-pen-on-sidetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    sofa - object
    sidetable2 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pen sofa)
    (at-location sidetable2 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location pen sidetable2)
  ))

  (:metric minimize (total-cost))
)