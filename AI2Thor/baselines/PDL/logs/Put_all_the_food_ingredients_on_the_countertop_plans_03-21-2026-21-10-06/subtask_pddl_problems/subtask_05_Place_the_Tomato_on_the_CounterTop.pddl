```pddl
(define (problem place-tomato-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tomato - object
    countertop1 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (at-location tomato floor)
    (not (holding robot1 tomato))
  )

  (:goal (and
    (at-location tomato countertop1)
  ))
)
```