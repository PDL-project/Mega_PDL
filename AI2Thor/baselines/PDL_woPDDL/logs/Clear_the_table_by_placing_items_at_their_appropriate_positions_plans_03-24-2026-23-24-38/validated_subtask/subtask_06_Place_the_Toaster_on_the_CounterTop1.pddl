(define (problem place-toaster-on-countertop1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    toaster - object
    diningTable - object
    counterTop1 - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 diningTable)
    (at-location toaster diningTable)
    (at-location counterTop1 floor)
    (not (holding robot1 toaster))
  )

  (:goal (and
    (at-location toaster counterTop1)
    (not (holding robot1 toaster))
  ))

  (:metric minimize (total-cost))
)