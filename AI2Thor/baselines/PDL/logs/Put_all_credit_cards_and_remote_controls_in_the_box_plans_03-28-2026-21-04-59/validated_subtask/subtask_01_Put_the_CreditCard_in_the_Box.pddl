(define (problem put-creditcard-in-box)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    creditcard - object
    box - object
    chair - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location creditcard chair)
    (at-location box floor)
    (object-close robot1 box)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location creditcard box)
    (object-close robot1 box)
  ))

  (:metric minimize (total-cost))
)