(define (problem put-spoon-in-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spoon - object
    drawer2 - object
    countertop - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location spoon countertop)
    (at-location drawer2 floor)
    (object-close robot1 drawer2)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location spoon drawer2)
    (object-close robot1 drawer2)
  ))

  (:metric minimize (total-cost))
)