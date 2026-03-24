```pddl
(define (problem place-bowl-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bowl1 - object
    countertop1 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 bowl1)
    (at-location countertop1 kitchen)
  )

  (:goal (and
    (at-location bowl1 countertop1)
  ))
)
```