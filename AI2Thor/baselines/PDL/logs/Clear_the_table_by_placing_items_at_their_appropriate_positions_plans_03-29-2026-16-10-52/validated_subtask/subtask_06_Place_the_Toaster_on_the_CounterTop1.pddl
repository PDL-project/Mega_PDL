(define (problem place-toaster-on-countertop1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    toaster - object
    diningTable - object
    counterTop1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location toaster diningTable)
    (at-location counterTop1 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location toaster counterTop1)
  ))

  (:metric minimize (total-cost))
)