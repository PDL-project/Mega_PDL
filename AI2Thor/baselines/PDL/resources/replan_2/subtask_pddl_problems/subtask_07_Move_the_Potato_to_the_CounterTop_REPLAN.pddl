```pddl
(define (problem move-potato-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    potato - object
    countertop1 - object
    bowl1 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 bowl1)
    (at-location potato kitchen)
    (not (object-close robot1 countertop1))
    (not (object-close robot1 bowl1))
  )

  (:goal (and
    (at-location potato countertop1)
  ))
)
```