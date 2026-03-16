(define (problem store-pen)
  (:domain allactionrobot)

  (:objects
    robot2 - robot
    pen - object
    armchair1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot2))
    (at robot2 kitchen)
    (holding robot2 pen)
    (object-close robot2 armchair1) ;; Assuming armchair1 is openable
  )

  (:goal (and
    (at-location pen armchair1)
    (not (holding robot2 pen))
    (object-close robot2 armchair1) ;; Ensure armchair1 is closed after placing the pen
  ))

  (:metric minimize (total-cost))
)