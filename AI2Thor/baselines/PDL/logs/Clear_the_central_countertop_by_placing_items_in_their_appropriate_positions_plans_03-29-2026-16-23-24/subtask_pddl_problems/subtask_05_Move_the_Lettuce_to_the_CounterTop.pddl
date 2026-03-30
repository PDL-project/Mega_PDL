```pddl
(define (problem move-lettuce-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    countertop - object
    countertop2 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location lettuce countertop)
    (at-location countertop2 floor)
  )

  (:goal (and
    (at-location lettuce countertop2)
  ))
)
```