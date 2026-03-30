(define (problem store-the-pillow)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pillow - object
    sofa - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pillow sofa)
    (at-location sofa floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location pillow sofa)
  ))

  (:metric minimize (total-cost))
)