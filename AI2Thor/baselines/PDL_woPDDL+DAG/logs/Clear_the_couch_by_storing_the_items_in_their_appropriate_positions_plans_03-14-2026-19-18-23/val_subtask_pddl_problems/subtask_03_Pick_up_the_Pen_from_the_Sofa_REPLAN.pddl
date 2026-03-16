(define (problem pick-up-pen)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    robot2 - robot
    pen - object
    pencil - object
    sofa - object
    floor - object
    sidetable - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (not (inaction robot2))
    (at robot1 sidetable)
    (at robot2 sofa)
    (at-location pen sofa)
    (holding robot2 pencil)
  )

  (:goal (and
    (holding robot2 pen)
  ))

  (:metric minimize (total-cost))
)