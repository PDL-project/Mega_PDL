```pddl
(define (problem place-tomato-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tomato - object
    countertop1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location tomato floor)
    (at-location countertop1 floor)
  )

  (:goal (and
    (at-location tomato countertop1)
  ))
)
```