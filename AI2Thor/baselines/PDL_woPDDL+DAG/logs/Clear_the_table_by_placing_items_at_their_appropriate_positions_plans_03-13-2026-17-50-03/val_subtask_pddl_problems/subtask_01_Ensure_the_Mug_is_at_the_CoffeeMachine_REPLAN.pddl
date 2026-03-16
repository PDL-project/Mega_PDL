(define (problem ensure-mug-at-coffeemachine)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    coffeemachine - object
    diningtable - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 coffeemachine)
    (at-location mug coffeemachine)
    (at-location coffeemachine diningtable)
    (not (holding robot1 mug))
  )

  (:goal (and
    (at-location mug coffeemachine)
    (not (holding robot1 mug))
  ))

  (:metric minimize (total-cost))
)