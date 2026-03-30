```pddl
(define (problem put-bowl-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bowl - object
    countertop2 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location bowl floor)
    (at-location countertop2 floor)
  )

  (:goal (and
    (at-location bowl countertop2)
  ))
)
```