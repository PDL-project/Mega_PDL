(define (problem move-plate-to-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    plate - object
    diningtable - object
    sofa - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location plate diningtable)
    (at-location sofa floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location plate sofa)
  ))

  (:metric minimize (total-cost))
)