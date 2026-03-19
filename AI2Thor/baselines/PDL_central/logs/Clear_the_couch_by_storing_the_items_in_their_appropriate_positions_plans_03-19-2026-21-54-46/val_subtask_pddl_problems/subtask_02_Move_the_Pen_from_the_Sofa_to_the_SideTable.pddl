(define (problem move-pen-to-sidetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    sofa - object
    sidetable - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pen sofa)
    (not (holding robot1 pen))
  )

  (:goal (and
    (at-location pen sidetable)
    (not (holding robot1 pen))
  ))

  (:metric minimize (total-cost))
)