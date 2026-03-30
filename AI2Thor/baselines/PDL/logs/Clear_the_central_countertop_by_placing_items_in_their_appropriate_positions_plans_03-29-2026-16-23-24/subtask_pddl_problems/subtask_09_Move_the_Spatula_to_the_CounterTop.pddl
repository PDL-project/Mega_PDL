```pddl
(define (problem move-spatula-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spatula - object
    countertop - object
    countertop2 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location spatula countertop)
    (at-location countertop2 floor)
  )

  (:goal (and
    (at-location spatula countertop2)
  ))
)
```