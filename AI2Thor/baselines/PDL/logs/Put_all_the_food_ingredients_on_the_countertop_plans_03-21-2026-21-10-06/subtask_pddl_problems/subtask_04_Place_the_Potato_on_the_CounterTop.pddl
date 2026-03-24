```pddl
(define (problem place-potato-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    potato - object
    countertop1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location potato floor)
    (not (holding robot1 potato))
  )

  (:goal (and
    (at-location potato countertop1)
  ))
)
```