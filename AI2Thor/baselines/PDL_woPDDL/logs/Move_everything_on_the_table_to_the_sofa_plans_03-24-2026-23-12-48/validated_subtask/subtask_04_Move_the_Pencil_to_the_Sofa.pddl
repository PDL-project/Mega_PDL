(define (problem move-pencil-to-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pencil - object
    diningtable - object
    sofa - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pencil diningtable)
    (not (holding robot1 pencil))
  )

  (:goal (and
    (at-location pencil sofa)
  ))

  (:metric minimize (total-cost))
)