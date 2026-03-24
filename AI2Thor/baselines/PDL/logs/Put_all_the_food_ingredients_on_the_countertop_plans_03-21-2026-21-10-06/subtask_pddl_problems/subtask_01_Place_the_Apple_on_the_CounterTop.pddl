```pddl
(define (problem place-apple-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    apple - object
    countertop1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location apple floor)
    (at-location countertop1 floor)
    (not (holding robot1 apple))
  )

  (:goal (and
    (at-location apple countertop1)
    (not (holding robot1 apple))
  ))
)
```