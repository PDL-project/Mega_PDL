(define (problem put-pen-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    diningtable - object
    sofa - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pen diningtable)
    (at-location sofa floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location pen sofa)
  ))

  (:metric minimize (total-cost))
)