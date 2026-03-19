(define (problem move-pillow-to-armchair)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pillow - object
    sofa - object
    armchair - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pillow sofa)
    (at-location armchair floor)
    (not (holding robot1 pillow))
  )

  (:goal (and
    (at-location pillow armchair)
    (not (holding robot1 pillow))
  ))

  (:metric minimize (total-cost))
)