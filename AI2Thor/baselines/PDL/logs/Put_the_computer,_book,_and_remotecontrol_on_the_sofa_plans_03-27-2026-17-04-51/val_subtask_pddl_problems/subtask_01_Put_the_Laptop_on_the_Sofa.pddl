(define (problem put-laptop-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    laptop - object
    diningtable - object
    sofa - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location laptop diningtable)
    (at-location sofa floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location laptop sofa)
  ))

  (:metric minimize (total-cost))
)