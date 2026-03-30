(define (problem put-spoon-in-drawer4)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spoon - object
    drawer4 - object
    countertop1 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 countertop1)
    (hand-empty robot1)
    (at-location spoon countertop1)
    (at-location drawer4 floor)
    (object-close robot1 drawer4)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location spoon drawer4)
    (object-close robot1 drawer4)
  ))

  (:metric minimize (total-cost))
)