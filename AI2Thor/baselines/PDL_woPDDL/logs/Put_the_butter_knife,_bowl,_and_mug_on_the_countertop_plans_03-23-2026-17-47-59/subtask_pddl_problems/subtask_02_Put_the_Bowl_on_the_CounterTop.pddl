```pddl
(define (problem put-bowl-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bowl - object
    countertop1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location bowl floor)
    (at-location countertop1 floor)
    (not (holding robot1 bowl))
  )

  (:goal (and
    (at-location bowl countertop1)
    (not (holding robot1 bowl))
  ))
)
```