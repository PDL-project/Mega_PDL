(define (problem put-ladle-in-drawer4)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    ladle - object
    drawer4 - object
    countertop - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location ladle countertop)
    (at-location drawer4 floor)
    (object-close robot1 drawer4)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location ladle drawer4)
    (object-close robot1 drawer4)
  ))

  (:metric minimize (total-cost))
)