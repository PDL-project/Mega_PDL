(define (problem store-pillow-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pillow - object
    sofa - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pillow sofa)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location pillow sofa)
  ))

  (:metric minimize (total-cost))
)