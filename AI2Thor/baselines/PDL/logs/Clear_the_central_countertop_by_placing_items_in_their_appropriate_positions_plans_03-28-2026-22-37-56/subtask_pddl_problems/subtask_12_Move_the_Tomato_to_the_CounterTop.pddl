```pddl
(define (problem move-tomato-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tomato - object
    countertop - object
    countertop2 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location tomato countertop)
    (at-location countertop2 floor)
  )

  (:goal (and
    (at-location tomato countertop2)
  ))
)
```