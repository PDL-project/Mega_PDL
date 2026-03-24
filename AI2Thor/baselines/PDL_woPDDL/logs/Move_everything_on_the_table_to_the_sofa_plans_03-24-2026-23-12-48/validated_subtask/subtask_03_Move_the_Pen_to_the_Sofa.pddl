(define (problem move-pen-to-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    diningtable - object
    sofa - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pen diningtable)
    (not (holding robot1 pen))
  )

  (:goal (and
    (at-location pen sofa)
    (not (holding robot1 pen))
  ))

  (:metric minimize (total-cost))
)