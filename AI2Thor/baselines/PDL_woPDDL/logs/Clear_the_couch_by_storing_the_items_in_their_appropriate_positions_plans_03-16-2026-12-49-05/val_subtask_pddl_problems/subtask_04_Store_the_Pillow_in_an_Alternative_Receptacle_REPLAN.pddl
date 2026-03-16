(define (problem store-pillow-in-alternative-receptacle)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pillow - object
    armchair1 - object
    sofa1 - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 sofa1)
    (holding robot1 pillow)
    (object-close robot1 armchair1) ;; Armchair is openable, starts closed
  )

  (:goal (and
    (at-location pillow armchair1)
    (not (holding robot1 pillow))
    (object-close robot1 armchair1) ;; Ensure armchair is closed after placing the pillow
  ))

  (:metric minimize (total-cost))
)