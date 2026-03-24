```pddl
(define (problem put-potato-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    potato - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (at-location potato countertop)
    (at-location countertop floor)
    (not (holding robot1 potato))
  )

  (:goal (and
    (at-location potato countertop)
    (not (holding robot1 potato))
  ))
)
```