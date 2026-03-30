```pddl
(define (problem move-potato-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    potato - object
    countertop - object
    countertop2 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location potato countertop)
    (at-location countertop2 floor)
  )

  (:goal (and
    (at-location potato countertop2)
  ))
)
```