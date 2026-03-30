(define (problem place-mug-on-coffeeMachine)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    coffeeMachine - object
    diningTable - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location mug diningTable)
    (at-location coffeeMachine diningTable)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location mug coffeeMachine)
  ))

  (:metric minimize (total-cost))
)