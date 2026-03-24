(define (problem move-plate-to-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    plate - object
    diningtable - object
    sofa - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location plate diningtable)
    (at-location sofa floor)
    (not (holding robot1 plate))
  )

  (:goal (and
    (at-location plate sofa)
    (not (holding robot1 plate))
  ))

  (:metric minimize (total-cost))
)